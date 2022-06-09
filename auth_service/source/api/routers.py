from flask import request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import (
    create_access_token, create_refresh_token, 
    jwt_required, get_jwt_identity
)

from marshmallow import ValidationError
from app import app
from utils import save_file
from models import User
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


@app.route("/api/auth/login", methods=["POST"])
def login():
    data = dict(request.form or request.json)
    username = data.get("username", None)
    password = data.get("password", None)
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))
        return jsonify(access_token=access_token, refresh_token=refresh_token)
    return jsonify({"msg": "Bad username or password"}), 401


    
@app.route("/api/auth/profile", methods=["GET"])
@jwt_required()
def user_profile():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@app.route("/api/auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)
