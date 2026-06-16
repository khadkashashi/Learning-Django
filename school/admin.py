from django.contrib import admin
from .models import Subject, Teacher, Student, Grade

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name','dob','email','phone']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name','dob','email']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name','short_name']
    search_fields = ['name']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['class_teacher','name']
    autocomplete_fields = ['subject']