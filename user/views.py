from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms import LoginForm, RegisterFrom
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    form = RegisterFrom()
    if request.method == "POST":
        form = RegisterFrom(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST["password"])
            user.save()
            return redirect("/admin")
    context = {"form": form}
    return render(request, "user/register.html", context)


def user_login(request):
    params = request.GET
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"],
            )
            if user is not None:
                if not user.is_staff:
                    return HttpResponse("you are not the staff")
                login(request, user)
                if params.get('next'):
                    return redirect(params.get('next'))
                return redirect('/admin')


    context = {"form": form}
    return render(request, "user/login.html", context)