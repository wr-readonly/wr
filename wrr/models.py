from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=20)
    moviesign=models.CharField(max_length=100)
