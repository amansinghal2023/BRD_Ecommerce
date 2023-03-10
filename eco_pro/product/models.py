from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    category_dic = models.TextField(blank=True)
    # image= models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_category=models.ManyToManyField('Category',related_name='category')
    product_name=models.CharField(max_length=100)
    product_dic=models.CharField(max_length=100)
    product_price=models.PositiveBigIntegerField()
    product_Image=models.URLField(null=True,blank=True)
    product_details=models.JSONField(null=True,blank=True,default=list)

    # def __str__(self):
    #     return self.product_category.name
    def __str__(self):
        return self.product_name
