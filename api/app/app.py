from flask import Flask
from instance.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
blacklist = set()

from app.routes import user_routes
from app.routes.rider_routes import rider_routes
from app.routes.driver_routes import driver_routes
from app.routes.trip_routes import trip_routes
from app.routes.user_routes import user_routes
from app.models import user, trip, driver, rider