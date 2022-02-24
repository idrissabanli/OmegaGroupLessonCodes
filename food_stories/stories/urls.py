from django.urls import path
from stories.views import home, recipes


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipes, name='recipes_page'),
]