from db_util import MongoDatabase
import os.path
import sys
import pytest
module_path = "../"
module_file = ""
path = os.path.join(module_path, module_file)
abs_path = os.path.abspath(path)
sys.path.append(abs_path)

# mo=MongoDatabase()
# mo.db_start()


def test_add1():
    x = 5
    y = 5
    assert x == y, "should pass"
