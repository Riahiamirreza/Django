from django.db import models
from register.serializers import UserSerializer
from django.contrib.auth.models import User


class Group2(models.Model):
    name = models.CharField(max_length=20)
    members = models.ManyToManyField(User)
    is_admin = models.BooleanField(default=False)


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'sender'
        )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='receiver'
        )
    text = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)