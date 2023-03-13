from .models import Profile,Address
from django.db.models import Q


def getprofile(data):
    data= data
    # print("I M IN SERVICE DATA -----------------------",data)
    for i in data:
        pro_lis=[]
        # print(i.get("address"))
        pro=i.get("address")
        pro_lis.append(pro)
        print("THIS IS PRO--------------------------- ",pro)
        pro_name=[]
        

        for j in pro_lis:
            name=list(Address.objects.filter(id=j).values())
        # list(Product.objects.filter(id = cart_obj.product[0]).values())

            # print("this is name is django --------------------------------------->",name)
            pro_name.append(name)
        # i["address"]=pro_name[0]
    return data

