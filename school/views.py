from django.shortcuts import render, redirect
from school.models import Student
from school.forms import StudentForm

# Create your views here.
def student_list(request):
    data = Student.objects.all()
    context = {
        "student":data
    }
    return render(request,'student/index.html',context)



def student_create(request):
    form = StudentForm()
    if request.method =="POST":
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/list')
    context = {
        "form":form
    }
    return render(request, 'student/create.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method =="POST":
        form = StudentForm(instance=student,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/list')
    context = {
        "form":form
    }
    return render(request, 'student/update.html', context)


def student_delete(request, id):
    student = Student.objects.get(id=id)  
    student.delete()
    return redirect('/student/list')