from .models import Profile,Address
from django.db.models import Q


def getprofile(data):
    data= data
    print("-----------------------",data)
    for i in data:
        print(i.get("address"))
        pro=i.get("adress")
        pro_name=[]

        for j in pro:
            name=Address.objects.get(id=j).name
            pro_name.append(name)
        i["address"]=pro_name
    return data

