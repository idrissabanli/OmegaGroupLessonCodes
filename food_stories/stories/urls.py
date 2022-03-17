from django.urls import path
from stories.views import home, recipes, stories, story_detail


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
    path('stories/', stories, name='stories_page'),
    path('stories/<int:id>/', story_detail, name='story_detail'),
]