from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, unique=True)
    text = models.TextField()