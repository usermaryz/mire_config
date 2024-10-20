import unittest
from unittest.mock import mock_open, MagicMock
from dz2 import DependencyVisualizer
import os
import subprocess

class TestDependencyVisualizer(unittest.TestCase):

    def test_get_dependencies_failure(self):
        # неуспешный HTTP-ответ
        mock_response = MagicMock()
        mock_response.status_code = 404
        
        visualizer = DependencyVisualizer('test_config.toml')
        
        # requests.get
        with unittest.mock.patch('requests.get', return_value=mock_response):
            with self.assertRaises(SystemExit):
                visualizer.get_dependencies('12345')

    def test_load_config(self):
        mock_file = mock_open(read_data='''
        [package]
        name = "loose-envify"
        [visualizer]
        graphviz_path = "/opt/homebrew/bin/dot"
        output_path = "dependency_graph.png"
        ''')
        
        with unittest.mock.patch('builtins.open', mock_file):
            visualizer = DependencyVisualizer('config.toml')

        self.assertEqual(visualizer.package_name, 'loose-envify')
        self.assertEqual(visualizer.graphviz_path, '/opt/homebrew/bin/dot')
        self.assertEqual(visualizer.output_path, 'dependency_graph.png')

    def test_get_dependencies_success(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = """
        <section id="tabpanel-dependencies">
            <ul class="list pl0">
                <li class="dib mr2">
                    <a href="/package/js-tokens" class="link">js-tokens</a>
                </li>
            </ul>
        </section>
        """
        
        visualizer = DependencyVisualizer('config.toml')
        
        with unittest.mock.patch('requests.get', return_value=mock_response):
            dependencies = visualizer.get_dependencies('loose-envify')

        self.assertIn('js-tokens', dependencies)

    def test_build_dependency_graph(self):
        visualizer = DependencyVisualizer('config.toml')
        with unittest.mock.patch.object(visualizer, 'get_dependencies', return_value={'js-tokens': ''}):
            graph = visualizer.build_dependency_graph()

        self.assertIn('loose-envify', graph)
        self.assertIn('js-tokens', graph['loose-envify'])

    def test_generate_png(self):
        # генерация PNG файла через Graphviz
        visualizer = DependencyVisualizer('config.toml')

        with unittest.mock.patch('subprocess.run') as mock_run:
            visualizer.generate_png('dependencies.dot')

            mock_run.assert_called_with(
                ['/opt/homebrew/bin/dot', '-Tpng', 'dependencies.dot', '-o', 'dependency_graph.png'],
                check=True
            )

    def test_save_graph_as_dot(self):
        # сохранение графа в .dot файл
        visualizer = DependencyVisualizer('config.toml')
        graph = {
            'loose-envify': ['js-tokens'],
        }

        mock_file = mock_open()
        with unittest.mock.patch('builtins.open', mock_file):
            visualizer.save_graph_as_dot(graph, 'dependencies.dot')

        mock_file().write.assert_any_call('digraph dependencies {\n')
        mock_file().write.assert_any_call('  "loose-envify" -> "js-tokens";\n')
        mock_file().write.assert_any_call('}\n')

if __name__ == '__main__':
    unittest.main()
