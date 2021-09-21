import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "2233qkadafgaufg"
    MONGODB_SETTINGS = {"db": "blog", "host": "localhost", "port": 27017}
