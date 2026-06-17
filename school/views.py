from django.shortcuts import render, redirect
from school.models import Grade, Student, Subject
from school.forms import StudentForm, SubjectForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
            return redirect('school/student/list')
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
            return redirect('/school/student/list')
    context = {
        "form":form
    }
    return render(request, 'student/create.html', context)



def grade_list(request):
    grade = Grade.objects.all()
    context = {
        "grade":grade
    }
    return render(request, 'grade/index.html',context)



# Subject class based view

class SubjectView(ListView):
    model = Subject
    template_name = "subject/index.html"
    context_object_name = "subject"


class SubjectCreateView(CreateView):
    model = Subject
    # fields = '__all__'
    form_class = SubjectForm
    template_name = "subject/create.html"
    success_url = "/school/subject/list"


class SubjectUpdateView(UpdateView):
    model = Subject
    # fields = '__all__'
    form_class = SubjectForm
    template_name = "subject/update.html"
    success_url = "/school/subject/list"