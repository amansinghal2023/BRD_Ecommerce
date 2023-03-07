from .models import Product,Category
from django.db.models import Q


def getcategory(data):
    data= data
    for i in data:
        print(i.get("product_category"))
        cat=i.get("product_category")
        cat_name=[]

        for j in cat:
            name=Category.objects.get(id=j).name
            cat_name.append(name)
        i["product_category"]=cat_name
    return data

# def getcategorybyid(data):
#     data= data
#     # v=data.get("product_category")
#     for i in data:
#         print(i.get("id"))
        # name=Category.objects.get(id=i).name
        # i["product_category"]=name
    # return data

        # print(i.get("id"))
        # print(type(i.id))
        # print(i.get("product_category"))
        # cat=i.get("product_category")
        # cat_name=[]

        # for j in cat:
        # name=Category.objects.get(id=i).name
        #     cat_name.append(name)
        
        # i["product_category"]=cat_name
    # return data

    # Category_name= Category.objects.get('name')
    # print(Category_name)
 
#  {
#             "id": 1,
#             "product_name": "Mobile",
#             "product_dic": "Its a phone",
#             "product_price": 12000,
#             "product_Image": "",
#             "product_category": [
#                 1
#             ]
#         },