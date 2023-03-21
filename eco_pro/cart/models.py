from django.db import models
from authentication.models import Signup
from product.models import Product
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Cart(models.Model):
    user= models.ForeignKey(Signup,on_delete=models.CASCADE)
    product= models.IntegerField()
    count=models.IntegerField(default=0)
    
# class ChessBoard(models.Model):
#     board = ArrayField(
#         ArrayField(
#             models.CharField(max_length=10, blank=True),
#             size=8,
#         ),
#         size=8,
#     )