# from django.db import models
# from django.contrib.auth.models import User
from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')

    # def __str__(self):
    #     return f"{self.user.username}'s profile"


    # def __str__(self):
    #     return f"{self.street}, {self.city}, {self.state} {self.zip_code}"

# Create your models here.
# class PersonalDetail(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     street_address_1 = models.CharField(max_length=100)
#     street_address_2 = models.CharField(max_length=100, blank=True)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     postcode = models.CharField(max_length=10)
#     country = models.CharField(max_length=50)

# class Profile(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Profile_category = models.CharField(default='User', max_length=100, blank=True)
#     # service = models.CharField(max_length=100, blank=True)
#     first_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     email = models.EmailField(max_length=150)
#     city = models.CharField(max_length=100, blank=True)
#     area = models.CharField(max_length=100, blank=True)
#     address = models.CharField(max_length=300, blank=True)

#     def __str__(self):
#         return self.user.username

# class City(models.Model):
#     city_id = models.IntegerField(primary_key=True)
#     city_name = models.CharField(max_length=500)
    
#     def __str__(self):
#         return self.city_name

        
# class Area(models.Model):
#     area_id = models.IntegerField(primary_key=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     area_name = models.CharField(max_length=500)

#     def __str__(self):
#         return self.area_name
    


###############################################################

