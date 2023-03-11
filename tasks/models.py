from django.db import models



class Task(models.Model):
    description = models.TextField()
    limit_date = models.DateField()
    status = models.TextChoices()