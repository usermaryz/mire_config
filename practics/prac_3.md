## Задание 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```
{
  groups: [ 
    "ИКБО-%d-20" % i for i in std.range(1, 24)
  ],

  students: [
    {
      age: 19,
      group: "ИКБО-4-20",
      name: "Иванов И.И."
    },
    {
      age: 18,
      group: "ИКБО-5-20",
      name: "Петров П.П."
    },
    {
      age: 18,
      group: "ИКБО-5-20",
      name: "Сидоров С.С."
    },
    {
      age: 18,
      group: "ИКБО-10-20",
      name: "Землянская М.М."
    }
  ],

  subject: "Конфигурационное управление"
}
```

<img width="1148" alt="Screenshot 2024-10-14 at 16 35 11" src="https://github.com/user-attachments/assets/d8bee74b-0472-47ab-b9ef-06d4ccf5c0b4">


## Задание 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let create_student : Natural -> Text -> Text -> Student =
	\(age : Natural) -> \(group : Text) -> \(name : Text) ->
  { age = age, group = group, name = name }

let create_group : Natural -> Group =
	\(num : Natural) ->
	"ИКБО-" ++ (Natural/show num) ++ "-20"

let groups : List Group = [ 
	create_group 1,
	create_group 2,
	create_group 3,
	create_group 4,
  create_group 5,
	create_group 6,
	create_group 7,
	create_group 8,
	create_group 9,
	create_group 10,
	create_group 11,
	create_group 12,
	create_group 13,
	create_group 14,
	create_group 15,
	create_group 16,
	create_group 17,
	create_group 18,
	create_group 19,
	create_group 20,
	create_group 21,
	create_group 22,
	create_group 23,
	create_group 24,
]

let students : List Student = [ 
	create_student 19 (create_group 4) "Иванов И.И.", 
	create_student 18 (create_group 4) "Петров П.П.",
	create_student 18 (create_group 5) "Сидоров С.С.",
	create_student 19 (create_group 10) "Землянская М.М."
]

let subject = "Конфигурационное управление"

in { groups = groups, students = students, subject = subject }

```
<img width="1246" alt="Screenshot 2024-10-14 at 16 35 37" src="https://github.com/user-attachments/assets/262a8446-9f48-4701-a8e1-7a3dbcebedc5">

## Задание 3
```py
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```

Язык нулей и единиц.
```
BNF = '''
E = 0 | 1 E | 1
'''
```
<img width="409" alt="Screenshot 2024-10-14 at 16 36 04" src="https://github.com/user-attachments/assets/6d43affd-b979-4cf1-9d30-abb74ef836f3">

## Задание 4
Язык правильно расставленных скобок двух видов.
```
BNF = '''
E = () | {} | ( E ) | { E } | E E
'''
```
<img width="446" alt="Screenshot 2024-10-14 at 16 36 47" src="https://github.com/user-attachments/assets/98fa1c12-1d29-4e4c-9629-85760f82df35">

## Задание 5
Язык выражений алгебры логики.
```
BNF = '''
E = E & E | E OR E | ~ E | ( E ) | x | y
'''
```
+ ```print(generate_phrase(parse_bnf(BNF), 'E').replace("OR", "|"))```

<img width="910" alt="Screenshot 2024-10-14 at 16 38 29" src="https://github.com/user-attachments/assets/6e51a184-3158-4e7d-9b26-bc77506538a5">

