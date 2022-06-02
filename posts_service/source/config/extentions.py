from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:12345@localhost:5432/posts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345' 

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

login_manager = LoginManager(app)

