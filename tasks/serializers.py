from rest_framework import serializers
from .models import Task
from projects.serializers import ProjectSerializer
class TaskSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'description', 'limit_date', 'status', 'project', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        

