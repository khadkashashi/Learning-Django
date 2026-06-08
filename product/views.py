from django.shortcuts import render,redirect
from product.models import Product
# Create your views here.

def product_list(request):
    data = Product.objects.all()
    return render(request, 'product/index.html',{"product":data})

def product_create(request):
    if request.method == "POST":
        data = request.POST
        product = Product.objects.create(
            name=data['name'],
            address=data['address'],
            phone =data['phone']
        )
        return redirect('/product-list')
    return render(request,'product/create.html')