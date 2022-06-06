from marshmallow import fields, validates, ValidationError, validates_schema
from config.extentions import ma
from models import User



class UserSchema(ma.SQLAlchemyAutoSchema):
    confirm_password = fields.String(load_only=True, required=True)
    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True
        include_fk = True

    # @validates_schema
    # def validate_object(self, data):
    #     print('here')
    #     print(data)
        # return data

    @validates('email')
    def email_validation(self, email):
        if User.query.filter_by(email=email):
            raise ValidationError("email must be unique")
        return True
    
    @validates('username')
    def username_validation(self, username):
        if User.query.filter_by(username=username):
            raise ValidationError("username must be unique")
        return True



    