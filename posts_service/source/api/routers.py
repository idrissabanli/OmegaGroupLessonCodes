from app import app
from models import Story
from schemas.story_schema import StorySchema


@app.route("/api/stories/")
def stories():
    story_list = Story.query.all()
    return StorySchema(many=True).jsonify(story_list), 200