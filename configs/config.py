import json

class ProductDatabase:
    SECRET_KEY = '\xa9\x9a@"\x86\xea\x1c\xce\x9a@\xbbF7\x01 )\xae\x98\xd0SH\xd7+f$\x13\x0f\xcf\xc5|6\xc1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_EXPIRATION = 3600

    def __init__(self):
        with open("configs/dbconfig.json") as file:
            dbconfig = json.loads(file.read())
            self.SQLALCHEMY_DATABASE_URI = (
                r"mysql+pymysql://{user}:{password}@" +
                r"{host}:{port}/{dbname}").format(**dbconfig)

class DevDatabase:
    SECRET_KEY = '\xa9\x9a@"\x86\xea\x1c\xce\x9a@\xbbF7\x01 )\xae\x98\xd0SH\xd7+f$\x13\x0f\xcf\xc5|6\xc1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_EXPIRATION = 3600

    def __init__(self):
        with open("configs/dev-dbconfig.json") as file:
            dbconfig = json.loads(file.read())
            self.SQLALCHEMY_DATABASE_URI = (
                r"mysql+pymysql://{user}:{password}@" +
                r"{host}:{port}/{dbname}").format(**dbconfig)

config = {
            'dev': DevDatabase,
            'product': ProductDatabase
         }