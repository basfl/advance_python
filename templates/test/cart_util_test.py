import os.path
import sys
import unittest
module_path = "../"
module_file = ""
path = os.path.join(module_path, module_file)
abs_path = os.path.abspath(path)
sys.path.append(abs_path)
from cart_util import cart_modify_template
from cart_util import cart_template


class TestCartUtil(unittest.TestCase):

    def test_1(self):
        self.assertEqual(cart_template(), 52)
    def test_2(self):
        self.assertEqual(cart_modify_template(), 52)

if __name__=="__main__":
    unittest.main()
