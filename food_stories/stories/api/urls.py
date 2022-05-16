from django.urls import path
from stories.api.views import StoryListCreateAPI, StoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('stories/', StoryListCreateAPI.as_view(),),
    # path('list-stories/', StoryListAPI.as_view(),),
    path('stories/<int:pk>/', StoryRetrieveUpdateDestroyAPIView.as_view(),),
]