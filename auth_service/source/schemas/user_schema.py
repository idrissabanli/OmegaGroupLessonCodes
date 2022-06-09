from marshmallow import fields, validates, ValidationError, validates_schema
from marshmallow.validate import Length
from config.extentions import ma
from models import User



class UserSchema(ma.SQLAlchemyAutoSchema):
    confirm_password = fields.String(load_only=True, required=True, validate=(Length(min=8),))
    password = fields.String(load_only=True, required=True, validate=(Length(min=8),))
    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True
        include_fk = True

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if not data["password"] == data["confirm_password"]:
            raise ValidationError('Confirm password is not same with password')


    @validates('email')
    def email_validation(self, email):
        if User.query.filter_by(email=email).first():
            raise ValidationError("email must be unique")
    
    @validates('username')
    def username_validation(self, username):
        if User.query.filter_by(username=username).first():
            raise ValidationError("username must be unique")



    