from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django.db.models.JSONField import JSONField


# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    item_cart=ArrayField(models.JSONField(),size=50, default=list ,blank=True,null=True)
    balance=models.IntegerField(null=True,default=0)

