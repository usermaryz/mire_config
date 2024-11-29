# вызов: python3 assembler.py tests/input.asm tests/output.bin tests/log.yaml

import yaml
import struct

def loadConstant(A, B):
    if not (0 <= A < 2**5) or not (0 <= B < 2**24):
        print("нарушен лимит разрядности")
    command_bits = (B << 5) | A
    return struct.pack("<I", command_bits)  # Формат big-endian

def readMemory(A, B):
    if not (0 <= A < 2**5) or not (0 <= B < 2**8):
        raise ValueError("нарушен лимит разрядности")
    command_bits = (B << 5) | A
    return struct.pack("<I", command_bits)

def writeMemory(A, B):
    if not (0 <= A < 2**5) or not (0 <= B < 2**8):
        raise ValueError("нарушен лимит разрядности")
    command_bits = (B << 5) | A
    return struct.pack("<I", command_bits)

def popcnt(A, B):
    if not (0 <= A < 2**5) or not (0 <= B < 2**27):
        raise ValueError("нарушен лимит разрядности")
    command_bits = (B << 5) | A
    return struct.pack("<I", command_bits)

def assemble(input_file, output_file, log_file):
    commands = []
    binary_data = bytearray()

    with open(input_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split()
        if not line:
            continue
        command, *args = line
        A = int(args[0])
        B = int(args[1])

        if command == 'LOAD_CONSTANT':
            binary_line = loadConstant(A, B)
        elif command == 'READ_MEMORY':
            binary_line = readMemory(A, B)
        elif command == 'WRITE_MEMORY':
            binary_line = writeMemory(A, B)
        elif command == 'POPCNT':
            binary_line = popcnt(A, B)
        else:
            raise ValueError(f"Неизвестная команда: {command}")

        commands.append({"command": command, "A": A, "B": B, "bytes": binary_line.hex()})
        binary_data.extend(binary_line)

    # Запись бинарного файла
    with open(output_file, "wb") as binfile:
        binfile.write(binary_data)

    # Запись YAML-лога
    with open(log_file, "w") as logfile:
        yaml.dump(commands, logfile, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Использование: python assembler.py <входной_файл> <выходной_файл> <лог_файл>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]
    assemble(input_file, output_file, log_file)