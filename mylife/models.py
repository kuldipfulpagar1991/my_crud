from django.db import models

# Create your models here.
class Mylife(models.Model):
    age=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
