from django.db import models

# Create your models here.

class user(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    #cart=models.aggregates_all()
    balance=models.IntegerField()
