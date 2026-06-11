from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name=models.CharField(50)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=80)
    hire_date=models.DateField(max_length=100)
    qulification=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        db_table="teacher"
class Student(models.Model):
    class_teacher=models.ForeignKey(Teacher,on_delete=models.RESTRICT,related_name="teacher_student")
    full_name=models.CharField(50)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=80)