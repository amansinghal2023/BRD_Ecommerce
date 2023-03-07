from django.db import models

# Create your models here.

class Signup(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    c_password=models.CharField(max_length=20)

'''
class Category(model.Models):
    name=models.CharField(max_length=100,unique=True)
    category_dic = models.TextField(blank=True)
    image= model.ImageField()

class Offer(model.Models):
    offer_id=model.Charfield()
    offer_dicount=models.DecimalField()

    
class Product(model.Models):
    product_category=model.Foreignkey(Category,on_delete=CASCADE.Do Nothing)
    product_name=models.CharField(max_length=100)
    product_dic=model.CharField(max_length=100)
    product_price=models.IntegerField()
    product_Image=models.ImageField()
    offer=models.ForeignKey(Offer,on_delete=CASCADE.Do Nothing)

'''