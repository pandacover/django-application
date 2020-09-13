from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    category = models.CharField(max_length=100)