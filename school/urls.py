from django.urls import path
from school.views import student_list, student_create, student_update, student_delete, grade_list,grade_create

urlpatterns = [
    path('student/list',student_list,name="student-list"),
    path('student/create',student_create,name="student-create"),
    path('student/update/<int:id>',student_update,name="student-update"),
    path('student/delete/<int:id>',student_delete,name="student-delete"),
    path('grade/list', grade_list, name="grade-list"),
    path('grade/create', grade_create, name="grade-create"),
    


]