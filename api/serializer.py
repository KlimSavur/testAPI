from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
