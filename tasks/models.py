from django.db import models


class Task(models.Model):
    description = models.TextField()
    limit_date = models.DateField()
    status = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name= 'tasks')

    def __repr__(self):
        return f'<[{self.id}] Task /{self.limit_date}>'
