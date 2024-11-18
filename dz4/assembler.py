import struct
import argparse
import yaml

# Функции для каждой команды
def load_constant(b):
    a = 30
    return struct.pack('>BH', (a | (b << 5)) & 0xFF, (b << 5) & 0xFFFF00)

def memory_read(b):
    a = 0
    return struct.pack('>BH', (a | (b << 5)) & 0xFF, (b << 5) & 0xFFFF00)

def memory_write(b):
    a = 8
    return struct.pack('>BH', (a | (b << 5)) & 0xFF, (b << 5) & 0xFFFF00)

def greater_than(b):
    a = 20
    return struct.pack('>BH', (a | (b << 5)) & 0xFF, (b << 5) & 0xFFFF00)

VALID_COMMANDS = {
    "LOAD_CONSTANT": load_constant,
    "MEMORY_READ": memory_read,
    "MEMORY_WRITE": memory_write,
    "GREATER_THAN": greater_than,
}

def assemble(input_file, output_file, log_file):
    logs = []
    with open(input_file, 'r') as infile, open(output_file, 'wb') as binfile:
        for line_num, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Ошибка в строке {line_num}: неверное количество аргументов.")

            command, b_value = parts[0], parts[1]
            if command not in VALID_COMMANDS:
                raise ValueError(f"Ошибка в строке {line_num}: недопустимая команда '{command}'.")

            try:
                b = int(b_value)
            except ValueError:
                raise ValueError(f"Ошибка в строке {line_num}: '{b_value}' не является целым числом.")

            command_func = VALID_COMMANDS[command]
            code = command_func(b)

            # Логирование данных
            log_entry = {
                "line": line_num,
                "command": command,
                "b": b,
                "machine_code": [f"0x{byte:02X}" for byte in code]
            }
            logs.append(log_entry)

            # Запись машинного кода в файл
            binfile.write(code)

    # Запись логов в YAML
    with open(log_file, 'w') as logfile:
        yaml.dump(logs, logfile, allow_unicode=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assembler for virtual machine.")
    parser.add_argument("input_file", help="Path to the input file with text program")
    parser.add_argument("output_file", help="Path to the output binary file")
    parser.add_argument("log_file", help="Path to the log YAML file")
    args = parser.parse_args()

    assemble(args.input_file, args.output_file, args.log_file)
