from config.extentions import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from slugify import slugify



class SaveMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    created_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(SaveMixin, UserMixin):
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    def save(self):
        self.password = generate_password_hash(self.password)
        return super().save()

