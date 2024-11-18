import struct
import argparse
import yaml

# Инициализация памяти и аккумулятора
MEMORY_SIZE = 1024
memory = [0] * MEMORY_SIZE
accumulator = 0

def interpret(binary_file, result_file, start, end):
    global accumulator
    logs = []

    with open(binary_file, 'rb') as binfile:
        while True:
            command = binfile.read(3)
            if not command:
                break

            # Распаковка команды
            a_b, b = struct.unpack('>BH', command)
            a = a_b % int("100000", 2)
            b = (b >> 5) + (a_b // int("100000", 2))

            # Выполнение команды
            if a == 30:  # LOAD_CONSTANT
                accumulator = b
                action = f"LOAD_CONSTANT: Set ACC to {b}"
            elif a == 0:  # MEMORY_READ
                accumulator = memory[b]
                action = f"MEMORY_READ: Read {accumulator} from memory[{b}]"
            elif a == 8:  # MEMORY_WRITE
                memory[b] = accumulator
                action = f"MEMORY_WRITE: Wrote {accumulator} to memory[{b}]"
            elif a == 20:  # GREATER_THAN
                memory[b] = 1 if memory[b] > accumulator else 0
                action = f"GREATER_THAN: memory[{b}] set to {memory[b]}"

            # Логирование действия
            logs.append({
                "a": a,
                "b": b,
                "action": action,
                "accumulator": accumulator,
                "memory_snapshot": memory[start:end + 1]
            })

    # Запись результата в YAML
    result_data = {
        "memory_dump": {f"mem[{i}]": memory[i] for i in range(start, end + 1)},
        "logs": logs
    }
    with open(result_file, 'w') as resfile:
        yaml.dump(result_data, resfile, allow_unicode=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interpreter for virtual machine.")
    parser.add_argument("binary_file", help="Path to the binary input file")
    parser.add_argument("result_file", help="Path to the result YAML file")
    parser.add_argument("start", type=int, help="Starting memory address to output")
    parser.add_argument("end", type=int, help="Ending memory address to output")
    args = parser.parse_args()

    interpret(args.binary_file, args.result_file, args.start, args.end)
