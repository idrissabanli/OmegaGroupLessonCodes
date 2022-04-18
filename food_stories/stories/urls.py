from django.urls import path
from stories.views import (
    home, recipes, stories, StoryDetailView,
    ContactView,
    StoryListView,
    like_story,
    liked_stories
)


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
    path('stories/', StoryListView.as_view(), name='stories_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('liked-stories/', liked_stories, name='liked_stories'),
    path('like/<int:id>/', like_story, name='like_story'),
    path('stories/<int:pk>/', StoryDetailView.as_view(), name='story_detail'),
]