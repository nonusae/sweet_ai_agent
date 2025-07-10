import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info_calculator(self):
        result = get_files_info('calculator', '.')
        print("Result for current directory:")
        print(result)

    def test_get_files_info_calculator_pkg(self):
        result = get_files_info('calculator', 'pkg')
        print("Result for 'pkg' directory:")
        print(result)

    def test_get_files_info_calculator_invalid(self):
        result = get_files_info('calculator', '/bin')
        print("Result for '/bin' directory:")
        print(result)

    def test_get_files_info_calculator_invalid_outside_dir(self):
        result = get_files_info('calculator', '../')
        print("Result for '../' directory:")
        print(result)

if __name__ == '__main__':
  unittest.main()
