from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    display = models.ImageField(upload_to='groups/', default='groups/group.png')
    description = models.TextField(default='Random group')
    police = models.TextField(default="999")
    health = models.TextField(default="213")
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Neighbourhood(models.Model):
#     Name = models.TextField()
#     display = models.ImageField(upload_to='groups/', default='groups/group.png')
#     admin = models.ForeignKey(User, on_delete=models.CASCADE)
#     description = models.TextField(default='Random group')
#     police = models.TextField(default="999")
#     health = models.TextField(default="213")
#
#     def __str__(self):
#         return self.Name
#
# class Business(models.Model):
#     Name = models.TextField()
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     show_my_email = models.BooleanField(default=True)
#     description = models.TextField(default='Local business')
#     neighbourhood = models.ForeignKey(Neighbourhood, related_name='biashara')
#
#     @property
#     def email(self):
#         return self.owner.user.email
#
#
# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Text = models.TextField()
#     neighbourhood = models.ForeignKey(Neighbourhood, related_name='posts')
