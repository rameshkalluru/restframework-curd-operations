from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publisher=models.CharField(max_length=30)

