from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import (CompletedTopicSerializer, TopicVideoSerializer,
TopicNoteSerializer)
from tracks.models import CompletedTopic, Topic
from rest_framework import status
from rest_framework.response import Response

class UserCompletedTopic(CreateAPIView):
    serializer_class = CompletedTopicSerializer

    def create(self, request, *args, **kwargs):
        try:
            topic = Topic.objects.get(slug=self.kwargs['slug'])
            try:
                CompletedTopic.objects.get(topic=topic)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except CompletedTopic.DoesNotExist:
                completed_topic = CompletedTopic.objects.create(user=request.user, topic=topic)
                serializer = self.get_serializer(completed_topic)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Topic.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class GetTopicVideoID(RetrieveAPIView):
    serializer_class = TopicVideoSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Topic.objects.all()

class GetTopicNote(RetrieveAPIView):
    serializer_class = TopicNoteSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Topic.objects.all()