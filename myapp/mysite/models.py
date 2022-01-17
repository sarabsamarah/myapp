from django.db import models

# Create your models here.


class Pose(models.Model):
    name= models.CharField(max_length=100)
    category= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    