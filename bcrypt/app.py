from encrypt_util import pass_encryption
if __name__ == "__main__":
    enc = pass_encryption()
    enc._password = input("please enter your password \n")
    pass_enc = enc.password_encryption()
    print(f"encryption is {pass_enc}")
