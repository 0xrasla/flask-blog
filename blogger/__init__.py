from flask import Flask
from blogger import config
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_object(config.Config)

db = MongoEngine()
db.init_app(app)

from blogger import routes
