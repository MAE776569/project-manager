from tracks.models import CompletedTopic
from rest_framework import serializers 

class CompletedTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTopic
        fields = '__all__'