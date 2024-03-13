from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Topic(models.Model):
    name=models.CharField(max_length=64)
    description=models.TextField(max_length=255)
    user=models.ManyToManyField(User, related_name='topics')

class Article(models.Model):
    title=models.CharField(max_length=255)
    text = models.TextField(max_length=10000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    topic=models.ManyToManyField(Topic, related_name='articles')
    
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=5000)
    article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user=models.ManyToManyField(User, related_name='comments')