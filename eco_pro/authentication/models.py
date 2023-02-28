from django.db import models

# Create your models here.

class Signup(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    c_password=models.CharField(max_length=20)


