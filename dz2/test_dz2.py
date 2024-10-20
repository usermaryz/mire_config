'''import unittest
import os
from dz2 import DependencyVisualizer

class TestDependencyVisualizer(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр визуализатора зависимостей с использованием тестового config.toml
        self.visualizer = DependencyVisualizer('config.toml')

    def test_load_config(self):
        # Тестирование загрузки конфигурационного файла
        config = self.visualizer.load_config('config.toml')
        self.assertIn('visualizer', config)

    def test_get_dependencies(self):
        # Создаем тестовую структуру пакета
        os.makedirs('test_package/node_modules/example_package', exist_ok=True)
        
        # Создаем тестовый файл package.json для основного пакета
        with open('test_package/package.json', 'w') as f:
            f.write('{"name": "test_package", "version": "1.0.0", "dependencies": {"example_package": "^1.0.0"}}')

        # Создаем тестовый файл package.json для зависимого пакета
        with open('test_package/node_modules/example_package/package.json', 'w') as f:
            f.write('{"name": "example_package", "version": "1.0.0", "dependencies": {}}')

        # Тестирование функции получения зависимостей
        deps = self.visualizer.get_dependencies('test_package')
        self.assertIn('example_package', deps)

    def test_build_dependency_graph(self):
        # Создаем тестовую структуру пакета
        os.makedirs('test_package/node_modules/example_package', exist_ok=True)
        
        # Создаем тестовый файл package.json для основного пакета
        with open('test_package/package.json', 'w') as f:
            f.write('{"name": "test_package", "version": "1.0.0", "dependencies": {"example_package": "^1.0.0"}}')

        # Создаем тестовый файл package.json для зависимого пакета
        with open('test_package/node_modules/example_package/package.json', 'w') as f:
            f.write('{"name": "example_package", "version": "1.0.0", "dependencies": {}}')

        # Тестирование построения графа зависимостей
        graph = self.visualizer.build_dependency_graph('test_package')
        self.assertIn('example_package', graph['test_package'])

    def test_save_graph_as_dot(self):
        # Тестирование сохранения графа в формате .dot
        graph = {'test_package': ['example_package'], 'example_package': []}
        self.visualizer.save_graph_as_dot(graph, 'test.dot')
        self.assertTrue(os.path.exists('test.dot'))

if __name__ == "__main__":
    unittest.main()
'''