from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    text = models.CharField(max_length=500)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    assignee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assigner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="assigner")




