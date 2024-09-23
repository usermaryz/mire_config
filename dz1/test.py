import unittest
import io
import sys
from dz1 import ShellEmulatorCLI
from pathlib import Path
from datetime import datetime

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.shell = ShellEmulatorCLI()

    def get_command_output(self, command, *args):
        original_stdout = sys.stdout
        capture = io.StringIO()
        sys.stdout = capture
        command(*args)
        sys.stdout = original_stdout
        output = capture.getvalue()
        return output

    def test_ls_root(self):
        output = self.get_command_output(self.shell.ls_command)
        self.assertIn('Documents', output)
        self.assertIn('Settings', output)
        self.assertIn('GitHub', output)

    def test_ls_documents(self):
        self.get_command_output(self.shell.cd_command, 'Documents')
        output = self.get_command_output(self.shell.ls_command)
        self.assertIn('file1.txt', output)
        self.assertIn('file2.txt', output)

    def test_cd_documents(self):
        self.get_command_output(self.shell.cd_command, 'Documents')
        self.assertEqual(self.shell.current_directory, './Documents')

    def test_cd_parent_directory(self):
        self.get_command_output(self.shell.cd_command, 'Documents')
        self.get_command_output(self.shell.cd_command, '..')
        self.assertEqual(self.shell.current_directory, '.')

    def test_cd_nonexistent_directory(self):
        output = self.get_command_output(self.shell.cd_command, 'Qwerty')
        self.assertIn("Error: Directory Qwerty not found", output)
            
    def test_date(self):
        output = self.get_command_output(self.shell.date_command)
        self.assertIn(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), output)
    
    def test_du_nonexistent_file(self):
        output = self.get_command_output(self.shell.du_command, "qwerty.txt")
        self.assertIn("Error: File qwerty.txt not found", output)

    def test_du_empty_file(self):
        self.get_command_output(self.shell.cd_command, 'Documents')
        self.get_command_output(self.shell.touch_command, 'new_file.txt')
        output = self.get_command_output(self.shell.du_command, "new_file.txt")
        self.assertIn("Size of new_file.txt: 0 bytes", output)

    def test_du_file(self):
        self.get_command_output(self.shell.cd_command, 'Documents')
        output = self.get_command_output(self.shell.du_command, "file1.txt")
        self.assertIn("Size of file1.txt: 27 bytes", output)

    def test_touch_file(self):
        self.get_command_output(self.shell.touch_command, 'new_file.txt')
        output = self.get_command_output(self.shell.ls_command)
        self.assertIn('new_file.txt', output)

if __name__ == '__main__':
    unittest.main()
