from django.shortcuts import render, redirect
from school.models import Student,Grade
from school.forms import StudentForm,GradeForm

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
            return redirect('/school/student/list')
    context = {
        "form":form
    }
    return render(request, '/school/student/create.html', context)


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method =="POST":
        form = StudentForm(instance=student,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/school/student/list')
    context = {
        "form":form
    }
    return render(request, '/school/student/update.html', context)

def student_delete(request, id):
    student = Student.objects.get(id=id)  
    student.delete()
    return redirect('/school/student/list')

def grade_list(request):
    grade = Grade.objects.all()
    context = {
        "grade":grade
    }
    return render(request, 'grade/index.html',context)

def grade_create(request):
    form = GradeForm()
    if request.method == "POST":
        form = GradeForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect('grade-list')
    context = {"form": form}
    return render(request, 'grade/create.html', context)
