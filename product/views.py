from django.shortcuts import render
from product.models import Product

# Create your views here.
def product_list(request):
    data=Product.objects.values('address','name')
    print(data)
    return render (request, 'product/index.html',{'Product':data} )