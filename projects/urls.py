from django.urls import path
from . import views


urlpatterns = [
    path('project/', views.ProjectView.as_view()),
    path('project/<int:id>/', views.DetailProjectView.as_view()),
]