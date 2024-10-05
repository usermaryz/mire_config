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

## Задание 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
```
let generateGroups = List/map Natural Text (\(i : Natural) -> "ИКБО-${Natural/show i}-20")
let groups = generateGroups (List/length (List/build Natural (\(f : Natural -> Text) -> 24)))
in { groups = groups
   , students =
     [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
     , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
     , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
     , { age = 18, group = "ИКБО-10-20", name = "Землянская М.М." }
     ]
   , subject = "Конфигурационное управление"
   }

```

## Задание 3
```
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

## Задание 4
Язык правильно расставленных скобок двух видов.
```
BNF = '''
E = () | {} | ( E ) | { E } | E E
'''
```

## Задание 5
Язык выражений алгебры логики.
```
BNF = '''
E = E & E | E OR E | ~ E | ( E ) | x | y
'''
```
+ ```print(generate_phrase(parse_bnf(BNF), 'E').replace("OR", "|"))```
