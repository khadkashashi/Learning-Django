from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    print("this is views")
    return HttpResponse("hello world")
def json_home(request):

   a={
       'name':"shashi",
       "add" : "palpa"
   }
   return JsonResponse(a)

def show_company(request):
    return render(request, "index.html",{"company":"aura"})
