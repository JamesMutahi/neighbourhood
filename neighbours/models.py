from django.contrib.auth.models import User
from django.db import models
from users.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighbourhood(models.Model):
    Name = models.TextField()
    display = models.ImageField(upload_to='groups/', default='groups/group.png')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default='Random group')
    police = models.TextField(default="999")
    health = models.TextField(default="213")

    def __str__(self):
        return self.Name

