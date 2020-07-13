from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_sent = models.DateTimeField(auto_now=True)
