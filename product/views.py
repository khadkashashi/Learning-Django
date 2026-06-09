from django.shortcuts import render,redirect
from product.forms import ProductForm
from product.models import Product
# Create your views here.

def product_list(request):
    data = Product.objects.all()
    return render(request, 'product/index.html',{"product":data})

# from django crm create view

# def product_create(request):
#     if request.method == "POST":
#         data = request.POST
#         product = Product.objects.create(
#             name=data['name'],
#             address=data['address'],
#             phone =data['phone']
#         )
#         return redirect('/product-list')
#     return render(request,'product/create.html')


def product_create(request):
    form = ProductForm()
    context = {
        "form":form
    }
    return render(request,'product/create2.html',context)