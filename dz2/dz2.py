import os
import subprocess
import toml
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

class DependencyVisualizer:
    def __init__(self, config_path):
        # Чтение конфигурации из TOML файла
        self.config = self.load_config(config_path)
        self.package_name = self.config['package']['name']
        self.graphviz_path = self.config['visualizer']['graphviz_path']
        self.output_path = self.config['visualizer']['output_path']

    def load_config(self, config_path):
        with open(config_path, 'r') as f:
            return toml.load(f)

    def get_dependencies(self, package_name):
        # Получаем зависимости из HTML страницы
        url = f'https://www.npmjs.com/package/{package_name}?activeTab=dependencies'
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Запрос выполнен успешно для {package_name}!")
            # Парсим HTML
            soup = BeautifulSoup(response.text, 'lxml')
            return self.parse_dependencies(soup)
        else:
            print(f"Ошибка при выполнении запроса для {package_name}: {response.status_code}")
            return {}

    def parse_dependencies(self, soup):
        # Извлекаем зависимости из элемента с id="tabpanel-dependencies"
        dependencies = {}
        tab_panel = soup.find(id="tabpanel-dependencies")
        
        if tab_panel:
            # Находим все зависимости в списке
            ul_element = tab_panel.find("ul", class_="list pl0")
            if ul_element:
                for item in ul_element.find_all("li", class_="dib mr2"):
                    dep_name = item.find("a", class_="link").text.strip()
                    dependencies[dep_name] = "unknown"  # Версия не указана, можно модифицировать для извлечения версии
            else:
                print("Список зависимостей не найден.")
        else:
            print("Элемент с id='tabpanel-dependencies' не найден.")
        return dependencies

    def build_dependency_graph(self, package_path):
        # Рекурсивно строим граф зависимостей
        graph = defaultdict(list)
        self._traverse_dependencies(package_path, self.package_name, graph)
        return graph

    def _traverse_dependencies(self, package_path, package_name, graph, visited=set()):
        # Если уже посетили этот пакет, возвращаемся, чтобы не зациклиться
        if package_name in visited:
            return

        # Добавляем пакет в посещённые
        visited.add(package_name)

        # Пытаемся получить зависимости пакета
        dependencies = self.get_dependencies(package_name)
        if not dependencies:
            print(f"Зависимости для {package_name} не найдены.")
            return

        # Добавляем зависимости в граф
        for dep in dependencies.keys():
            graph[package_name].append(dep)
            # Рекурсивно обрабатываем зависимости
            self._traverse_dependencies(package_path, dep, graph, visited)

        # Проверяем существование node_modules и обрабатываем подпакеты
        node_modules_path = os.path.join(package_path, 'node_modules')
        if os.path.exists(node_modules_path):
            for sub_package in os.listdir(node_modules_path):
                sub_package_path = os.path.join(node_modules_path, sub_package)
                if os.path.isdir(sub_package_path):
                    # Обрабатываем подпакеты
                    self._traverse_dependencies(sub_package_path, sub_package, graph, visited)

    def save_graph_as_dot(self, graph, dot_file_path):
        # Генерация .dot файла для Graphviz
        with open(dot_file_path, 'w') as f:
            f.write('digraph dependencies {\n')
            for pkg, deps in graph.items():
                for dep in deps:
                    f.write(f'  "{pkg}" -> "{dep}";\n')
            f.write('}\n')

    def generate_png(self, dot_file_path):
        # Генерация PNG файла с использованием Graphviz
        subprocess.run([self.graphviz_path, '-Tpng', dot_file_path, '-o', self.output_path], check=True)

    def visualize(self, package_path):
        # Визуализация графа зависимостей
        print(f"Starting visualization for package {self.package_name}...")
        graph = self.build_dependency_graph(package_path)
        dot_file_path = 'dependencies.dot'
        self.save_graph_as_dot(graph, dot_file_path)
        self.generate_png(dot_file_path)
        print(f"Graph successfully saved to {self.output_path}")


if __name__ == "__main__":
    visualizer = DependencyVisualizer('config.toml')
    # Замените 'path_to_your_node_modules' на фактический путь к вашей папке node_modules
    visualizer.visualize('path_to_your_node_modules')
