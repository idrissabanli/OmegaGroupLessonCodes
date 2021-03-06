from marshmallow import fields
from config.extentions import ma
from models import Story, Category, Tag, User


class UserSchema(ma.SQLAlchemyAutoSchema):
    email = fields.Email(required=True)

    class Meta:
        model = User
        load_instance = True
        include_fk = True


class CategorySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Category
        load_instance = True
        include_fk = True
        exclude = ('created_at', )


class TagSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Tag
        load_instance = True
        include_fk = True
        exclude = ('created_at', )



class StorySchema(ma.SQLAlchemyAutoSchema):
    category = fields.Nested(CategorySchema, )
    tags = fields.Nested(TagSchema, many=True)
    slug = fields.String(dump_only=True)

    class Meta:
        model = Story
        load_instance = True
        include_fk = True