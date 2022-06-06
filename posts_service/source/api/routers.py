from flask import request, jsonify
from marshmallow import ValidationError
from app import app
from models import Story
from utils import save_file
from schemas.story_schema import StorySchema


@app.route("/api/stories/", methods=['GET', 'POST'])
def stories():
    if request.method == 'POST':
        image = request.files['image']
        image_path = save_file(image)
        if not image_path:
            return jsonify({ 'message': 'Something went wrong'}), 400
        data = dict(request.form or request.json)
        data['image'] = image_path
        try:
            schema = StorySchema().load(data)
            schema.save()
        except ValidationError as err:
            return err.messages, 400
        return StorySchema().jsonify(schema), 201
    story_list = Story.query.all()
    return StorySchema(many=True).jsonify(story_list), 200