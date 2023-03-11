from django.db import models

class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
       return f'< [{self.id}] {self.name} ({self.created_at})>'

