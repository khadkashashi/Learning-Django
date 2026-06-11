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
    if request.method =="POST":
        data = request.POST
        form = ProductForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/product-list')

    context = {
        "form":form
    }

    return render(request,'product/create2.html',context)


def product_update(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        data =request.POST
        form = ProductForm(instance=product,data=data)
        if form.is_valid():
            form.save()
            return redirect('/product-list')

    context = {
        "form":form
    }

    return render(request,'product/update.html',context)


def product_delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/product-list')