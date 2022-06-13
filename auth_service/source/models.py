import requests
from config.extentions import db, login_manager
from flask import url_for, render_template
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from slugify import slugify
from utils import generate_confirmation_token
from publisher import Publish


@login_manager.user_loader
def load_user(user):
    return User.get(user)


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
    is_active = db.Column(db.Boolean, nullable=True, default=False)

    def save(self):
        self.password = generate_password_hash(self.password)
        return super().save()

    def send_data_post_service(self):
        from schemas.user_schema import UserSchema
        data = UserSchema().dump(self)
        requests.post(url='http://127.0.0.1:5003/api/save-user/', json=data)

    def send_confirmation_mail(self):
        token = generate_confirmation_token(email=self.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirmation_mail.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        data = {
            'body': html,
            'subject': subject,
            'subtype': 'html',
            'recipients': [self.email,]
        }
        Publish(data=data, event_type='send_mail')


