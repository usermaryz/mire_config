## Задача1
```
pip show matplotlib
```
<img width="571" alt="image" src="https://github.com/user-attachments/assets/45e633f0-3a07-4d05-8400-f1acfbaac1c0">

### Основные элементы:
Name: Название пакета — matplotlib.  
Version: Текущая установленная версия пакета — 3.7.2.  
Summary: Краткое описание пакета — "Python plotting package" (пакет для построения графиков в Python).  
Home-page: Домашняя страница пакета — https://matplotlib.org, на которой можно найти документацию и ресурсы по использованию.  
Author: Авторы пакета — John D. Hunter (создатель matplotlib) и Michael Droettboom.  
Author-email: Электронная почта для связи с авторами — matplotlib-users@python.org.  
License: Тип лицензии — PSF (Python Software Foundation License).  
Location: Путь на локальной машине, где установлен пакет — /Users/mary/anaconda3/lib/python3.11/site-packages.  
Requires: Зависимости, необходимые для работы пакета:  
contourpy  
cycler  
fonttools  
kiwisolver  
numpy  
packaging  
pillow  
pyparsing  
python-dateutil  
Required-by: Пакеты, которые зависят от matplotlib. В данном случае это пакет seaborn — библиотека для визуализации данных.  

### Как получить пакет без менеджера пакетов
```
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
python setup.py install
```

## Задача2
```
npm view express
```
<img width="569" alt="image" src="https://github.com/user-attachments/assets/48fb078b-93c1-47f3-9af2-be785177bd5e">

### Основные элементы:  
express@4.21.0: Название пакета и версия — express@4.21.0.  
MIT: Лицензия пакета — MIT License (свободная лицензия).  
deps: 31: Количество зависимостей — 31.  
versions: 279: Количество версий пакета в репозитории — 279.  
Fast, unopinionated, minimalist web framework: Описание пакета — Быстрый, минималистичный веб-фреймворк.  
dist: Метаданные о дистрибутиве:  
.tarball: Ссылка на архив пакета — express-4.21.0.tgz  
.shasum: Хеш SHA1 для проверки целостности — d57cb706d49623d4ac27833f1cbc466b668eb915.  
.integrity: Хеш SHA512 для безопасности — sha512-VqcNGcj/....  
.unpackedSize: Размер распакованного пакета — 220.8 kB.  
dependencies: Список зависимостей, например:  
accepts@~1.3.8  
body-parser@1.20.3  
cookie@0.6.0  
maintainers: Список людей, поддерживающих пакет:  
wesleytodd <wes@wesleytodd.com>  
dougwilson <doug@somethingdoug.com>  
dist-tags: Метки для версий:  
latest: 4.21.0  
next: 5.0.0  

### Как получить пакет без менеджера пакетов
```
git clone https://github.com/expressjs/express.git
cd express
npm install
```


## Задача3
```python
import graphviz

# Создание графа зависимостей с помощью graphviz
dot = graphviz.Digraph(
    comment="Dependencies for matplotlib and plotly.express")

# Зависимости matplotlib
dot.node('matplotlib', 'matplotlib')
dot.node('numpy', 'numpy')
dot.node('cycler', 'cycler')
dot.node('kiwisolver', 'kiwisolver')
dot.node('pyparsing', 'pyparsing')
dot.node('python_dateutil', 'python_dateutil')

# Добавление ребер для matplotlib
dot.edge('matplotlib', 'numpy')
dot.edge('matplotlib', 'cycler')
dot.edge('matplotlib', 'kiwisolver')
dot.edge('matplotlib', 'pyparsing')
dot.edge('matplotlib', 'python_dateutil')

# Общие зависимости
dot.edge('numpy', 'pandas')

# Сохранение и рендеринг графа
output_path = 'dependencies_graph'
dot.render(output_path, format='png')

print(f"Граф сохранен в файл: {output_path}.png")
```
![dependencies_graph](https://github.com/user-attachments/assets/42169f3c-d0c1-46ca-b133-9b0fe8139946)


```python
import graphviz

# Создание графа зависимостей с помощью graphviz
dot = graphviz.Digraph(
    comment="Dependencies for matplotlib and plotly.express")

# Зависимости plotly.express
dot.node('plotly.express', 'plotly.express')
dot.node('plotly', 'plotly')
dot.node('pandas', 'pandas')
dot.node('scipy', 'scipy')

# Добавление ребер для plotly.express
dot.edge('plotly.express', 'plotly')
dot.edge('plotly', 'pandas')
dot.edge('plotly', 'numpy')
dot.edge('plotly', 'scipy')

# Общие зависимости
dot.edge('numpy', 'pandas')

# Сохранение и рендеринг графа
output_path = 'dependencies_graph'
dot.render(output_path, format='png')

print(f"Граф сохранен в файл: {output_path}.png")
```
![dependencies_graph](https://github.com/user-attachments/assets/61f019db-0724-4603-b99f-1adf7e626167)


## Задача4
```minizinc
include "globals.mzn";

% Определяем билет как массив из 6 цифр, каждая из которых от 0 до 9
array[1..6] of var 0..9: ticket;

% Левая и правая части билета (по 3 цифры)
var int: left_sum = ticket[1] + ticket[2] + ticket[3];
var int: right_sum = ticket[4] + ticket[5] + ticket[6];

% Все цифры билета должны быть различны
constraint all_different(ticket);

% Сумма левой части должна быть равна сумме правой части
constraint left_sum = right_sum;

% Определение целевой функции - минимизация суммы всех цифр (можно минимизировать, например, сумму цифр билета)
solve minimize (ticket[1]+ticket[2]+ticket[3]);
```

<img width="353" alt="Снимок экрана 2024-09-20 в 10 49 17 PM" src="https://github.com/user-attachments/assets/e6ed054c-a1ed-4501-b8d8-cb9a2383e7f1">


## Задача5
```
enum Package = {root, menu, dropdown, icons};

array[Package] of int: num_versions = [1, 6, 5, 2];

array[Package] of var 1..6: selected_version;

% root зависит от menu >= 1.1.0, icons >= 1.0.0 (все версии)
constraint selected_version[root] = 1 -> 
    (selected_version[menu] >= 2 /\ selected_version[dropdown] >= 2 /\ selected_version[icons] >= 1);

% menu 1.1.0 и выше зависит от dropdown >= 2.0.0, icons >= 2.0.0
constraint selected_version[menu] >= 2 -> 
    (selected_version[dropdown] >= 2 /\ selected_version[icons] >= 2);

solve satisfy;

output [
    "root: ", show(selected_version[root]), "\n",
    "menu: ", show(selected_version[menu]), "\n",
    "dropdown: ", show(selected_version[dropdown]), "\n",
    "icons: ", show(selected_version[icons]), "\n"
];

```

## Задача6
```
enum Package = {root, foo, left, right, shared, target};

array[Package] of int: num_versions = [1, 2, 1, 1, 2, 2];

array[Package] of var 1..2: selected_version;

constraint selected_version[root] = 1 -> 
    (selected_version[foo] >= 1 /\ selected_version[foo] <= 2 /\
     selected_version[target] = 2);

constraint selected_version[foo] = 2 -> 
    (selected_version[left] = 1 /\ selected_version[right] = 1);

constraint selected_version[left] = 1 -> selected_version[shared] >= 1;

constraint selected_version[right] = 1 -> selected_version[shared] < 2;

constraint selected_version[shared] = 1 -> selected_version[target] = 1;

solve satisfy;

output [
    "root: ", show(selected_version[root]), "\n",
    "foo: ", show(selected_version[foo]), "\n",
    "left: ", show(selected_version[left]), "\n",
    "right: ", show(selected_version[right]), "\n",
    "shared: ", show(selected_version[shared]), "\n",
    "target: ", show(selected_version[target]), "\n"
];
```
<img width="504" alt="image" src="https://github.com/user-attachments/assets/65d7e0d9-b3e3-476d-8657-ccb453173701">


## Задача7
```
```
