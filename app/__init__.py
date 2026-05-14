from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

app = Flask(__name__)

# Database
app.config.from_object(Config)

# Initialize DB
db = SQLAlchemy(app)
# Initialize MA
ma = Marshmallow(app)

from app import models, routes