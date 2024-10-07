## Задача 1
```
pip show matplotlib
```
<img width="571" alt="11" src="https://github.com/user-attachments/assets/6646ca48-b76b-4a7c-b514-4a5accc67e25">

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

## Задача 2
```
npm view express
```
<img width="569" alt="222" src="https://github.com/user-attachments/assets/b9e23d92-eabb-4aba-b897-752d2a9c2bfc">

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


## Задача 3
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
![33](https://github.com/user-attachments/assets/1d7b7a0d-bc9f-4408-9ab3-72975e876878)


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
![44](https://github.com/user-attachments/assets/f73b0796-dd30-4f51-8424-e46a03c08108)


## Задача 4
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
<img width="353" alt="55" src="https://github.com/user-attachments/assets/96b377d1-b533-4b85-8741-f6c8c101bea9">


## Задача 5
```
array [1..2] of var 0..1: icons_package;
array [1..6] of var 0..1: menu_package;
array [1..5] of var 0..1: dropdown_package;

var 1..2: selected_icons;
var 1..6: selected_menu;
var 1..5: selected_dropdown;

constraint sum(icons_package) = 1;
constraint sum(menu_package) = 1;
constraint sum(dropdown_package) = 1;

constraint icons_package[2] = 0;

constraint menu_package[1] = dropdown_package[1];

constraint forall(v in 2..6)(
  menu_package[v] <= dropdown_package[2] + dropdown_package[5]
);

constraint forall(v in 2..5)(
  dropdown_package[v] <= icons_package[2]
);

constraint forall(v in 1..2)(
  if icons_package[v] == 1 
  then selected_icons = v 
  else true endif
);

constraint forall(v in 1..6)(
  if menu_package[v] == 1 
  then selected_menu = v 
  else true endif
);

constraint forall(v in 1..5)(
  if dropdown_package[v] == 1 
  then selected_dropdown = v 
  else true endif
);

output [
  "icons: ", show(selected_icons), "\n",
  "menu: ", show(selected_menu), "\n",
  "dropdown: ", show(selected_dropdown)
];
```
<img width="240" alt="Снимок экрана 2024-10-06 в 6 31 20 PM" src="https://github.com/user-attachments/assets/71ac2efa-4006-4a4b-9d88-47f4b6d5e36a">


## Задача 6
```
enum Version = {v100, v110, v200};  % Версии 1.0.0, 1.1.0, 2.0.0
enum Package = {root, foo, target, left, right, shared};

array[Package] of set of Version: available_versions = [
  {v100},        % root
  {v100, v110},  % foo
  {v100, v200},  % target
  {v100},        % left
  {v100},        % right
  {v100, v110, v200}   % shared
];

array[Package] of var Version: installed_version;

constraint (installed_version[root] = v100) -> (installed_version[foo] in {v100, v110} /\
                                                 installed_version[target] = v200);

constraint (installed_version[foo] = v110) -> (installed_version[left] = v100 /\
                                                installed_version[right] = v100);

constraint (installed_version[foo] = v100);

constraint (installed_version[left] = v100) -> (installed_version[shared] in {v100, v110, v200});

constraint (installed_version[right] = v100) -> (installed_version[shared] in {v100, v110});

constraint (installed_version[shared] = v200) -> true;

constraint (installed_version[shared] = v110) -> true;

constraint (installed_version[shared] = v100) -> (installed_version[target] in {v100});

constraint (installed_version[target] = v200) -> true;
constraint (installed_version[target] = v100) -> true;

output [
  "Installed versions:\n",
  "foo: ", show(installed_version[foo]), "\n",
  "target: ", show(installed_version[target]), "\n",
  "left: ", show(installed_version[left]), "\n",
  "right: ", show(installed_version[right]), "\n",
  "shared: ", show(installed_version[shared]), "\n"
];
```
<img width="253" alt="Снимок экрана 2024-10-06 в 6 46 35 PM" src="https://github.com/user-attachments/assets/7f909fc8-9c13-4ce2-af37-225745924d17">

## Задача 7
```
```
