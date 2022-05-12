from django.urls import path
from stories.api.views import StoryAPI

urlpatterns = [
    path('stories/', StoryAPI.as_view(),),
]