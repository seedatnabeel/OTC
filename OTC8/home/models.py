# from django.db imp
from django.db import models
class Symptoms(models.Model):
    sympt = models.CharField(max_length=100)

class Post(models.Model):
    title=models.CharField(max_length=128)
    content=models.TextField()

