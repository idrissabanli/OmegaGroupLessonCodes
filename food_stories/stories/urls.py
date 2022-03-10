from django.urls import path
from stories.views import home, recipes, stories


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
    path('stories/', stories, name='stories_page'),
]