from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    groups = models.JSONField(default={"all_groups":[]})

class Group(models.Model):
    groupname = models.CharField(max_length=500, unique = True)
    users = models.JSONField(default={"all_users":[]})

    def add_user(new_user):
        # is this the right way to retrieve and update JSON ??
        __all_users = self.users['all_users']
        self.users['all_users'] = __all_users + [new_user.username]
        self.save()

        new_user.groups['all_groups'] = new_user.groups['all_groups'] + [self.groupname]
        new_user.save()
        return

    @classmethod
    def create(cls, name, creator):
        group = cls(groupname=name)
        group.add_user(creator)
        return group

    