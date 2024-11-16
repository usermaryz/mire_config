import re
import json
import sys

class ConfigParser:
    def __init__(self):
        self.variables = {}

    def remove_comments(self, text):
        # многострочные комментарии
        return re.sub(r'/#.*?#/', '', text, flags=re.DOTALL)

    def parse_var(self, line):
        # var имя значение
        match = re.match(r'^\s*var\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+(.+)$', line)
        if match:
            var_name, var_value = match.groups()
            evaluated_value = self.evaluate_value(var_value.strip())
            self.variables[var_name] = evaluated_value
            return var_name, evaluated_value
        return None

    def evaluate_value(self, value):
        # @"строка"
        if value.startswith('@\"') and value.endswith('\"'):
            return value[2:-1]  # Извлекаем строку из @"строка"
        # $имя$
        elif value.startswith('$') and value.endswith('$'):
            var_name = value[1:-1]
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise ValueError(f"Undefined variable: {var_name}")
        # числовые значения
        elif re.match(r'^\d+$', value):
            return int(value)
        # массивы [значение; значение; ...]
        elif value.startswith('[') and value.endswith(']'):
            return self.parse_array(value)
        else:
            return value

    def parse_array(self, value):
        # квадратные скобки и элементы массива
        value = value.strip()[1:-1]
        elements = []
        for v in value.split(';'):
            v = v.strip()
            if v:
                evaluated_element = self.evaluate_value(v)
                elements.append(evaluated_element)
        return elements

    def parse_line(self, line):
        line = line.strip()
        if not line:
            return None
        var_result = self.parse_var(line)
        if var_result:
            var_name, var_value = var_result
            return var_name, var_value
        match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s+\$([a-zA-Z_][a-zA-Z0-9_]*)\$$', line)
        if match:
            key, var_name = match.groups()
            if var_name in self.variables:
                return key, self.variables[var_name]
            else:
                raise ValueError(f"Undefined variable: {var_name}")
        # строки с массивом значений
        match = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s+\[(.*)\]$', line)
        if match:
            key, array_body = match.groups()
            elements = self.parse_array(f"[{array_body}]")
            return key, elements
        else:
            raise ValueError(f"Invalid line format: {line}")

    def parse_config(self, config_text):
        config_text = self.remove_comments(config_text)
        result = {}
        for line in config_text.splitlines():
            try:
                parsed_line = self.parse_line(line)
                if parsed_line:
                    key, value = parsed_line
                    result[key] = value
            except Exception as e:
                print(f"Error: {e}")
        # self.variables в итоговый результат
        for key, value in self.variables.items():
            if key not in result:
                result[key] = value
        return result

def main():
    input_text = sys.stdin.read()
    parser = ConfigParser()
    try:
        parsed_data = parser.parse_config(input_text)
        print(json.dumps(parsed_data, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
