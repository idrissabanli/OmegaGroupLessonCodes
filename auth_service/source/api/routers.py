from flask import request, jsonify
from marshmallow import ValidationError
from app import app
from utils import save_file
from schemas.user_schema import (
    UserSchema
)

@app.route("/api/auth/register/", methods=['POST'])
def register():
    image = request.files['image']
    image_path = save_file(image)
    if not image_path:
        return jsonify({ 'message': 'Something went wrong'}), 400
    data = dict(request.form or request.json)
    data['image'] = image_path
    try:
        schema = UserSchema().load(data)
        schema.save()
    except ValidationError as err:
        return err.messages, 400
    return UserSchema().jsonify(schema), 201

