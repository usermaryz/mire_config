## Задача 1
```bash
cat /etc/passwd | sort
```
<img width="798" alt="Screenshot 2024-09-02 at 16 35 58 (1)" src="https://github.com/user-attachments/assets/0ef3cb81-d7d4-4002-a9c0-e6493df323ec">


## Задача 2
```bash
cat /etc/protocols | awk '{print $2, $1}' | sort -nr |head -n 5
```

<img width="844" alt="Screenshot 2024-09-02 at 17 08 30 (1)" src="https://github.com/user-attachments/assets/2f8949c2-6322-4c90-a22b-9e33daae00f5">


## Задача 3
```bash
#!bin/bash

word="$1"
length=${#word}
border="+-"
for ((i=0; i<length; i++)); do
    border="$border-"
done
border="$border-+"
echo $border
echo "| $word |"
echo $border
```

<img width="424" alt="Screenshot 2024-09-02 at 17 48 27 (1)" src="https://github.com/user-attachments/assets/6d29c95d-897f-4232-8601-c59762b3eaf6">


## Задача 4
```bash
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort | uniq | tr '\n' ' '
```

<img width="768" alt="Снимок экрана 2024-09-09 в 2 13 41 AM" src="https://github.com/user-attachments/assets/f7d09545-f513-4a9f-8837-d7983a66784d">


## Задача 5

```bash
#!/bin/bash

chmod +x "$1"
sudo mv "$1" /usr/local/bin/
```

## Задача 6
```
#!/bin/bash
file=$1
first_line=$(head -n 1 "$file")

if [[ "$file" =~ \.(c|js)$ ]]; then
    if [[ "$first_line" =~ ^\s*\/\/ ]] || [[ "$first_line" =~ ^\s*\/\* ]]; then
        echo "[$file] have comment"
    else
        echo "[$file] no comment"
    fi
elif [[ "$file" =~ \.py$ ]]; then
    if [[ "$first_line" =~ ^\s*# ]]; then
        echo "[$file] have comment"
    else
        echo "[$file] no comment"
    fi
fi
```

## Задача 7

```bash
#!/bin/bash
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
```

## Задача 8

```bash
#!/bin/bash

find . -type f -name "*.$1" | tar -cvf "$2" -T -
```


## Задача 9

```bash
#!/bin/bash

sed 's/    /\t/g' "$1" > "$2"
```

## Задача 10

```bash
#!/bin/bash

# Директория для поиска пустых текстовых файлов
dir=$1

find "$dir" -type f -name "*.txt" -empty
```


