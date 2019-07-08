import os.path
import sys
import pytest
import bcrypt
module_path = "../"
module_file = ""
path = os.path.join(module_path, module_file)
abs_path = os.path.abspath(path)
sys.path.append(abs_path)
from encrypt_util import pass_encryption


@pytest.fixture
def supply_data():
    return["my password"]


def test_pass_encrypt(supply_data):
    enc = pass_encryption()
    enc.password = supply_data[0]
    enc_pass = enc.password_encryption()
    print(f"the encryption is {enc_pass}")
    result = bcrypt.checkpw(enc.password, enc_pass)
    assert result == True
