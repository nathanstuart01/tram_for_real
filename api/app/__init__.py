from flask import Flask
from instance.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes import home_route