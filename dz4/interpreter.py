#вызов: python3 interpreter.py tests/output.bin  tests/result.yaml

import struct
import yaml
import sys
import traceback

stack = [0]*16
memory = [0]*1024

def indetif_command(start, end):
    return ((1<<(end-start+1))-1)<<start

def load_constant(b):
    stack.append(b)

def read_memory(b):
    if not stack:
        print("Стек пуст")
    address = stack.pop() + b
    print(address)
    stack.append(memory[address])

def write_memory(b):
    if len(stack) < 2:
        print("Недостаточно элементов в стеке")
    address = stack.pop() + b
    memory[address] = stack.pop()

def unary_popcnt(b):
    if not stack:
        print("Стек пуст")
    value = stack.pop()
    memory[b] = bin(value).count("1")

def get_operand(chunk, start, end):
    return (int.from_bytes(chunk)&indetif_command(start, end)) >> start

def execute(command, chunk):
    if command == 16:  # Загрузка константы
        b = get_operand(chunk, 5, 27)
        load_constant(b)
    elif command == 7:  # Чтение из памяти
        b = get_operand(chunk, 5, 11)
        read_memory(b)
    elif command == 23:  # Запись в память
        b = get_operand(chunk, 5, 11)
        write_memory(b)
    elif command == 10:  # Унарная операция popcnt
        b = get_operand(chunk, 5, 30)
        unary_popcnt(b)
    else:
        print(f"Неизвестная команда: {command}")

def get_state():
    return {
        "stack": stack,
        "memory": memory,
    }

def parse_binary(file_path):
    with open(file_path, "rb") as f:
        while chunk := bytearray(f.read(4)):  # Читаем по 4 байта
            chunk.reverse()
            command = chunk[-1]&indetif_command(0, 4)
            execute(command, chunk)

def main():
    if len(sys.argv) < 3:
        print("Использование: python interpetor.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        parse_binary(input_file)
    except Exception as e:
        print(traceback.print_exc())
        sys.exit(1)

    # Сохранение состояния в YAML
    with open(output_file, "w") as f:
        yaml.dump(get_state(), f)

    print(f"Результат сохранен в {output_file}")

if __name__ == "__main__":
    main()