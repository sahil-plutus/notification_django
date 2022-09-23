from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Chat_Group(models.Model):
    class Meta:
        verbose_name = "Chat Group"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Chat(models.Model):
    user = models.ForeignKey(User, related_name='chat', on_delete=models.CASCADE)
    content = models.CharField(max_length=1222)
    timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Chat_Group, related_name='chat', on_delete=models.CASCADE)
