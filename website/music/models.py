from django.db import models

class Symptoms(models.Model):
    sympt = models.CharField(max_length=100)