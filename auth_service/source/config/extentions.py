import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost:5433/auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345' 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

login_manager = LoginManager(app)

