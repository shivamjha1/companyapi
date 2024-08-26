from django.db import models

# Create your models here.

class Employees(models.Model):
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
    intern=models.BooleanField(null=True)
    
