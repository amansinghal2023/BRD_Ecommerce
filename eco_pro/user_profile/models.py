# from django.db import models
# from django.contrib.auth.models import User
from django.db import models
from django.db import models
# from django.contrib.auth.models import User

from authentication.models import Signup

class Profile(models.Model):
   
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    date_of_birth = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.first_name

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)