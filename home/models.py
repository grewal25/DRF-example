from django.db import models


class Post(models.Model):
    topic = models.CharField(max_length = 40)
    author = models.CharField(max_length = 40)
    body = models.TextField()