from django.urls import path
from stories.views import (
    home, recipes, stories, story_detail,
    contact_page,
    like_story,
    liked_stories
)


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
    path('stories/', stories, name='stories_page'),
    path('contact/', contact_page, name='contact_page'),
    path('liked-stories/', liked_stories, name='liked_stories'),
    path('like/<int:id>/', like_story, name='like_story'),
    path('stories/<int:id>/', story_detail, name='story_detail'),
]