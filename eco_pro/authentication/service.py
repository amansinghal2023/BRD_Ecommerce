from .models import Signup
from django.db.models import Q


def validate_password(password,c_password):
    if password!=c_password and len(password)<8:
        return False
    else:
        return True
    
def user_validation(email,password):
    obj=Signup.objects.filter(Q(email=email) & Q(password=password)).values()
    print(obj)
    if len(obj)==0:
        return False
    else:
        return True