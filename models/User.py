import bcrypt

class User:
    name = ""
    user_name = ""
    password = ""

    # parameterized constructor 
    def __init__(self, name, user_name, password): 
        self.name = name 
        self.user_name = user_name
        self.password = password

    def hashPassword(self):
        hashpass = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        self.password = hashpass
        return self

    def toJson(self):
        return {
            "name": self.name,
            "user_name": self.user_name,
            "password": self.password
        }