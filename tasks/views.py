from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response
from django.shortcuts import get_object_or_404
from .serializers import TaskSerializer
from projects.models import Project
from .models import Task


class TaskView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        project_id = self.kwargs.get('id')
        project_instance = get_object_or_404(Project, pk=project_id)
        return serializer.save(project=project_instance)

    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('id')
        project = get_object_or_404(Project, pk=project_id)
        tasks = Task.objects.filter(project = project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class DetailTaskView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

