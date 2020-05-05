""" changing the path of the current folder
to the main/root folder 
"""
import os.path
import sys
module_path = "../"
module_file = ""
path = os.path.join(module_path, module_file)
abs_path = os.path.abspath(path)
sys.path.append(abs_path)
print("path is {}".format(abs_path))
from scrapy import Scarpy
import unittest


class TestSCrapy(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        sc = Scarpy()
        sc.scrapy_function()


if __name__ == "__main__":
    unittest.main()
