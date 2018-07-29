from tracks.models import CompletedTopic, Topic
from rest_framework import serializers 

class CompletedTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTopic
        fields = '__all__'

class TopicVideoSerializer(serializers.ModelSerializer):
    video_id = serializers.CharField(source='get_video_id')
    class Meta:
        model = Topic
        fields = ['video_id']

class TopicNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['note']