import os
import tarfile
import csv
from datetime import datetime

class ShellEmulatorCLI:
    def __init__(self, root=None):
        self.root = root
        self.load_config("config.csv")
        self.current_directory = "."  # начальная директория
        self.file_system = {}
        self.load_virtual_file_system()  #загрузка виртуальной файловой системы
        self.display_prompt()

    def load_config(self, config_file):
        # загрузка конфигурации эмулятора из csv файла
        with open(config_file, 'r') as f:
            reader = csv.reader(f)
            config = list(reader)
            self.username = config[0][0]
            self.fs_archive = config[0][1]

    def load_virtual_file_system(self):
        # загрузка виртуальной файловой системы из архива .tar.
        if tarfile.is_tarfile(self.fs_archive):
            with tarfile.open(self.fs_archive, "r") as tar:
                for member in tar.getmembers():
                    self.file_system['./' + member.name] = member
        else:
            print("Error: .tar archive not found")

    def display_prompt(self):
        print(f"{self.username}@virtual_shell:{self.current_directory}$ ", end='')

    def process_command(self):
        # введенные команды.
        command = input()
        
        if command.startswith("ls"):
            self.ls_command()
        elif command.startswith("cd"):
            exit()
        elif command.startswith("touch"):
            exit()
        elif command == "date":
            exit()
        elif command.startswith("du"):
            exit()
        elif command == "exit":
            exit()
        else:
            print(f"Command not found: {command}")
        
        self.display_prompt()

    def ls_command(self):
        # ls: содержимое текущего каталога
        exit()

    def cd_command(self, path):
         # cd: изменение текущего каталога
         exit()

    def touch_command(self, filename):
        # touch: создание нового файла
        exit()

    def date_command(self):
        # date: текущая дата и время
        exit()

    def du_command(self, path):
        # du: размер указанного файла или директории
        exit()


if __name__ == "__main__":
    shell = ShellEmulatorCLI()
    while True:
        shell.process_command()