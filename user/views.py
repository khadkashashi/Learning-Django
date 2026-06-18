from django.shortcuts import render, redirect
from user.forms import RegisterFrom
# Create your views here.
def register(request):
    form = RegisterFrom()
    if request.method == "POST":
        form = RegisterFrom(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST['password'])
            user.save()
            return redirect('/admin')
    context = {
        "form":form
    }
    return render(request, 'user/register.html',context)