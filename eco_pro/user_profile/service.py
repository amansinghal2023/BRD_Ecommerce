from .models import Profile,Address
from authentication.models import Signup
from django.db.models import Q

def getprofile(data):
    data= data
    print("-----> this is data from getprofile function",data)
    for i in data:
        print(i.get("signup_profile"))
        cat=i.get("signup_profile")
        cat_name=[]
        for j in range(0,cat+1):
            if j==cat:
                name=Signup.objects.get(id=j).email
                cat_name.append(name)
                i["signup_profile"]=cat_name
    return data

    # data= data
    # for i in data:
    #     pro_lis=[]
    #     pro=i.get("address")
    #     pro_lis.append(pro)
    #     print("THIS IS PRO--------------------------- ",pro)
    #     pro_name=[]
    #     for j in pro_lis:
    #         name=list(Address.objects.filter(id=j).values())
    #         pro_name.append(name)
    # return data

