## Задание 1
${Землянская М М}$
$\int_{x}^{\infty} \frac{dt}{t(t^2-1) \log t} = \int_{x}^{\infty} \frac{1}{t \log t} \left( \sum_{m} t^{-2m} \right) dt = \sum_{m} \int_{x}^{\infty} \frac{t^{-2m}}{t \log t} dt \overset{(u=t^{-2m})}{=} - \sum_{m} \text{li}(x^{-2m})$

## Задание 2
![image](https://github.com/user-attachments/assets/c0c9e216-ebbf-4254-ac99-fc30fcafa06b)

```uml
@startuml
actor "Землянская М М" as student
database Piazza as piazza
actor Преподаватель as teacher


teacher -> piazza : Публикация задачи
activate piazza
piazza --> teacher : Задача опубликована
deactivate piazza
...

student -> piazza : Поиск задач
activate piazza
piazza --> student : Получение задачи
deactivate piazza
...

student -> piazza : Публикация решения
activate piazza
piazza --> student : Решение опубликовано
deactivate piazza
...

teacher -> piazza : Поиск решений
activate piazza
piazza --> teacher : Решение найдено

teacher -> piazza : Публикация оценки
piazza --> teacher : Оценка опубликована
deactivate piazza
...

student -> piazza : Проверка оценки
activate piazza
piazza --> student : Оценка получена
deactivate piazza

@enduml
```

## Задание 3

## Задание 4

## Задание 5
