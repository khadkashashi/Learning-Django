from django.urls import path
from school.views import student_list, student_create, student_update, grade_list,grade_create, grade_update, SubjectView, SubjectCreateView, SubjectUpdateView,student_delete

urlpatterns = [
    path('student/list',student_list,name="student-list"),
    path('student/create',student_create,name="student-create"),
    path('student/update/<int:id>',student_update,name="student-update"),
     path('student/delete/<int:id>',   student_delete, name='student-delete'), 
    path('grade/list', grade_list, name="grade-list"),
     path('grade/create', grade_create, name="grade-create"),
      path('grade/update/<int:id>', grade_update, name="grade-update"),
    path('subject/list',SubjectView.as_view(), name="subject-list"),
    path('subject/create',SubjectCreateView.as_view(), name="subject-create"),
    path('subject/update/<int:pk>',SubjectUpdateView.as_view(), name="subject-update"),



]