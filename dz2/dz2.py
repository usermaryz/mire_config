from time import sleep
import sys
import subprocess
import toml
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

class DependencyVisualizer:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.package_name = self.config['package']['name']
        self.graphviz_path = self.config['visualizer']['graphviz_path']
        self.output_path = self.config['visualizer']['output_path']

    def load_config(self, config_path):
        with open(config_path, 'r') as f:
            return toml.load(f)

    def get_dependencies(self, package_name):
        url = f'https://www.npmjs.com/package/{package_name}?activeTab=dependencies'
        for i in range(5):
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Запрос выполнен успешно для {package_name}!")
                soup = BeautifulSoup(response.text, 'lxml')
                return self.parse_dependencies(soup)
            elif response.status_code == 404:
                print(f"Библиотеки {package_name} не существует")
                sys.exit()
            else:
                sleep(5)
        else:
            print(f"Ошибка при выполнении запроса для {package_name}: {response.status_code}")
            return {}

    def parse_dependencies(self, soup):
        # id="tabpanel-dependencies"
        dependencies = {}
        tab_panel = soup.find(id="tabpanel-dependencies")
        
        if tab_panel:
            # все зависимости в списке
            ul_element = tab_panel.find("ul", class_="list pl0")
            if ul_element:
                for item in ul_element.find_all("li", class_="dib mr2"):
                    dep_name = item.find("a", class_="link").text.strip()
                    dependencies[dep_name] = ""
            else:
                print("Список зависимостей не найден.")
        else:
            print("Элемент с id='tabpanel-dependencies' не найден.")
        return dependencies

    def build_dependency_graph(self):
        # граф зависимостей
        graph = defaultdict(list)
        self._traverse_dependencies(self.package_name, graph)
        return graph

    def _traverse_dependencies(self, package_name, graph, visited=set()):
        if package_name in visited:
            return

        visited.add(package_name)

        dependencies = self.get_dependencies(package_name)
        if not dependencies:
            print(f"Зависимости для {package_name} не найдены.")
            return

        for dep in dependencies.keys():
            graph[package_name].append(dep)
            self._traverse_dependencies(dep, graph, visited)

    def save_graph_as_dot(self, graph, dot_file_path):
        with open(dot_file_path, 'w') as f:
            f.write('digraph dependencies {\n')
            for pkg, deps in graph.items():
                for dep in deps:
                    f.write(f'  "{pkg}" -> "{dep}";\n')
            f.write('}\n')

    def generate_png(self, dot_file_path):
        subprocess.run([self.graphviz_path, '-Tpng', dot_file_path, '-o', self.output_path], check=True)

    def visualize(self):
        print(f"Starting visualization for package {self.package_name}...")
        graph = self.build_dependency_graph()
        dot_file_path = 'dependencies.dot'
        self.save_graph_as_dot(graph, dot_file_path)
        self.generate_png(dot_file_path)
        print(f"Graph successfully saved to {self.output_path}")


if __name__ == "__main__":
    visualizer = DependencyVisualizer('config.toml')
    visualizer.visualize()
