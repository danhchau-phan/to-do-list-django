from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS_CHOICES = [
        ('Not started', 'Not started'),
        ('Just started', 'Just started'),
        ('Almost done', 'Almost done'),
        ('Done', 'Done'),
    ]

    description = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=500, default='Not started', choices = STATUS_CHOICES)
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assigner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="assigner")




