from django.db import models
# from django.contrib.auth.models import User
from config import settings
User = settings.base.AUTH_USER_MODEL
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title