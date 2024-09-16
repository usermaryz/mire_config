## Задача1
```
pip show matplotlib
```
<img width="571" alt="image" src="https://github.com/user-attachments/assets/45e633f0-3a07-4d05-8400-f1acfbaac1c0">


## Задача2
```
npm view express
```
<img width="569" alt="image" src="https://github.com/user-attachments/assets/48fb078b-93c1-47f3-9af2-be785177bd5e">


## Задача3

## Задача4

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
