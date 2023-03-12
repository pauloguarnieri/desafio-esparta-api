from django.urls import path
from . import views


urlpatterns = [
    path('task/project/<int:id>/', views.TaskView.as_view()),
    path('task/<int:id>/', views.DetailTaskView.as_view()),
    
]