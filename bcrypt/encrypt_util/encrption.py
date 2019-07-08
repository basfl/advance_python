import bcrypt


class pass_encryption:
    @property
    def password(self):
        return self._password

    # @password.setter
    @password.setter
    def password(self, v):
        self._password = v

    def password_encryption(self):

        self.hashed = bcrypt.hashpw(
            self._password.encode('utf8'), bcrypt.gensalt())
        return self.hashed
