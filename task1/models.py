from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')

    def __str__(self):
        return self.title