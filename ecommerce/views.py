from django.shortcuts import render

# Create your views here.
def ecommerce_sites(request):
    return render(request, 'ecommerce/index.html' , {'best':'welcome to daraz nepal'})
