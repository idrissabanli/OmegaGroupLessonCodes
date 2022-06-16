from flask import request, jsonify
from marshmallow import ValidationError
from flask_jwt_extended import (
    create_access_token, create_refresh_token, 
    jwt_required, get_jwt_identity, verify_jwt_in_request
)
# from api.auth import jwt_required_or_readonly
from flasgger import swag_from
from app import app
from models import Story
from utils import save_file
from schemas.story_schema import StorySchema, UserSchema

def jwt_required_or_readonly(f):
    def wrapper():
        if request.method == 'GET':
            return f()
        verify_jwt_in_request()
        return f()
    return wrapper


@app.route("/api/stories/<int:id>/", methods=['GET', 'POST'])
@swag_from('docs/get_stories.yml', methods=['GET'])
@swag_from('docs/create_story.yml', methods=['POST'])
@jwt_required_or_readonly
def get_stories(id):
    if request.method == 'POST':
        image = request.files.get('image', None)
        data = dict(request.form) or request.get_json(silent=True) or dict()
        image_path = None
        if image:
            image_path = save_file(image)
            if not image_path:
                return jsonify({ 'message': 'Something went wrong'}), 400
        
        data['image'] = image_path
        try:
            data['author_id'] = get_jwt_identity()
            schema = StorySchema().load(data)
            schema.save()
        except ValidationError as err:
            return err.messages, 400
        return StorySchema().jsonify(schema), 201
    story_list = Story.query.all()
    return StorySchema(many=True).jsonify(story_list), 200



@app.route("/api/save-user/", methods=['POST'])
def save_user():
    data = dict(request.form or request.json)
    print(data)
    try:
        user = UserSchema().load(data)
        user.save()
        print('user', user)
    except ValidationError as err:
        print(err.messages)
        return err.messages, 400
    return UserSchema().jsonify(user), 201

