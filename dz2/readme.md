## Домашнее задание 2
Инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости.

### Требования:
- Python 3.6+
- Установленный Graphviz
- Установленные Python-библиотеки:
  - `requests`
  - `beautifulsoup4`
  - `lxml`
  - `toml`

### Установка зависимостей:
1. Клонируйте репозиторий или скопируйте файлы.
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # для Linux/macOS
    .venv\Scripts\activate  # для Windows
    ```
3. Установите необходимые библиотеки:
    ```bash
    pip install -r requirements.txt
    ```

4. Убедитесь, что Graphviz установлен и доступен через команду `dot`. Для macOS это можно сделать через Homebrew:
    ```bash
    brew install graphviz
    ```

1. Отредактируйте файл конфигурации `config.toml` для указания нужного NPM-пакета и пути к установленному Graphviz:
    ```toml
    [package]
    name = "loose-envify"  # Имя NPM пакета

    [visualizer]
    graphviz_path = "/opt/homebrew/bin/dot"  # Путь к Graphviz (можно проверить командой `which dot`)
    output_path = "dependency_graph.png"  # Путь для сохранения PNG файла
    ```

2. Запустите скрипт:
    ```bash
    python dz2.py
    ```

## Тестирование

Для тестирования проекта используйте встроенные юнит-тесты. Они помогут убедиться, что функции программы работают корректно.

1. Запуск всех тестов:
    ```bash
    python -m unittest test_dz2.py
    ```

2. Основные тесты включают:
    - **`test_get_dependencies_failure`**: Проверка поведения при несуществующем пакете (HTTP 404).
    - **`test_load_config`**: Проверка загрузки конфигурационного файла.
    - **`test_get_dependencies_success`**: Проверка успешного извлечения зависимостей.
    - **`test_build_dependency_graph`**: Проверка построения графа зависимостей.
    - **`test_generate_png`**: Проверка генерации PNG файла через Graphviz.
    - **`test_save_graph_as_dot`**: Проверка сохранения графа в формате `.dot`.

## Структура проекта

- `dz2.py` — основной скрипт, содержащий логику программы.
- `test_dz2.py` — юнит-тесты для проверки функциональности.
- `config.toml` — файл конфигурации для указания параметров пакета и путей.
- `requirements.txt` — список зависимостей Python.

## Пример визуализированного графа

Пример PNG файла с графом зависимостей для пакета `loose-envify`:

![dependency_graph](https://github.com/user-attachments/assets/97ae899e-2c34-461e-8fa7-ca6ed0f0a066)
