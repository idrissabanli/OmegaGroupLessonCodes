from rest_framework.views import APIView
from rest_framework.response import Response

from stories.api.serializers import StoryReadSerializer, StoryCreateSerializer
from stories.models import Story


class StoryAPI(APIView):

    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()
        serializer = StoryReadSerializer(stories, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StoryCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)