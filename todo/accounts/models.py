from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Group(models.Model):
    groupname = models.CharField(max_length=500, unique = True)
    users = models.ManyToManyField(User)

    def add(new_user):
        self.users.add(new_user)
        self.save()
        return

    @classmethod
    def create(cls, name, creator):
        group = cls(groupname=name)
        group.add(creator)
        return group

    