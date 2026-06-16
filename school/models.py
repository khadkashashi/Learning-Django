from django.db import models



'''

    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    hire_date DATE,
    department_id INT,
    qualification VARCHAR(100),
    salary DECIMAL(10,2),

'''
# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=80)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=80)
    hire_date = models.DateTimeField()
    qualification = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "teacher"

    def __str__(self):
        return self.full_name

class Student(models.Model):
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,related_name="teacher_student")
    full_name = models.CharField(max_length=80)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=80)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.full_name
    
