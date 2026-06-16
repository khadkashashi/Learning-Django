from django.urls import path
from school.views import student_list, student_create, student_update

urlpatterns = [
    path('list',student_list,name="student-list"),
    path('create',student_create,name="student-create"),
    path('update/<int:id>',student_update,name="student-update"),


]