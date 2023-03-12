from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProjectSerializer
from .models import Project


class ProjectView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

   
class DetailProjectView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = 'id'