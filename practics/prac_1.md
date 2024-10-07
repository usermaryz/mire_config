## Задача 1
```bash
cat /etc/passwd | sort
```
<img width="798" alt="1" src="https://github.com/user-attachments/assets/9ab65f29-05eb-4e54-a2a9-1410fa391085">



## Задача 2
```bash
cat /etc/protocols | awk '{print $2, $1}' | sort -nr |head -n 5
```
<img width="844" alt="2" src="https://github.com/user-attachments/assets/7c60baab-a1c0-42d9-8ae6-cb492a30e92b">


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
<img width="424" alt="3" src="https://github.com/user-attachments/assets/790ce2c8-d800-4325-bbd9-b3d5e9372450">


## Задача 4
```bash
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort | uniq | tr '\n' ' '
```
<img width="768" alt="4" src="https://github.com/user-attachments/assets/e5911897-1d0e-46bf-ab52-d3d9b410ea5c">


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
