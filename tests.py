import unittest
from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.run_python import run_python_file

class MainTest(unittest.TestCase):
    # def test_get_files_info_calculator(self):
    #     result = get_files_info('calculator', '.')
    #     print("Result for current directory:")
    #     print(result)

    # def test_get_files_info_calculator_pkg(self):
    #     result = get_files_info('calculator', 'pkg')
    #     print("Result for 'pkg' directory:")
    #     print(result)

    # def test_get_files_info_calculator_invalid(self):
    #     result = get_files_info('calculator', '/bin')
    #     print("Result for '/bin' directory:")
    #     print(result)

    # def test_get_files_info_calculator_invalid_outside_dir(self):
    #     result = get_files_info('calculator', '../')
    #     print("Result for '../' directory:")
    #     print(result)

    # def test_get_file_content_calculator_main(self):
    #     print(get_file_content("calculator", "lorem.txt"))
    #     print(get_file_content('calculator', 'main.py'))
    #     print(get_file_content('calculator', 'pkg/calculator.py'))
    #     print(get_file_content('calculator', '/bin/cat'))

    # def test_write_file_calculator_main(self):
    #     print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    #     print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    #     print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    def test_run_python(self):
        print(run_python_file("calculator", "main.py"))
        print(run_python_file("calculator", "tests.py"))
        print(run_python_file("calculator", "../main.py"))
        print(run_python_file("calculator", "nonexistent.py"))

if __name__ == '__main__':
    unittest.main()
