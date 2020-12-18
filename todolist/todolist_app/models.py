from django.db import models

# Create your models here.
class ListItem(models.Model):
    text = models.CharField(max_length = 200)
    checked = False