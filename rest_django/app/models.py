from django.db import models
from django.forms import CharField

# Create your models here.
class god(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    village=models.CharField(max_length=40)