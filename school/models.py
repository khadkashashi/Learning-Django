from django.db import models



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
    class_teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name="teacher_student"
    )
    full_name = models.CharField(max_length=80)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=80)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.full_name


class Subject(models.Model):
    name = models.CharField(max_length=10)
    short_name = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = "subject"

    def __str__(self):
        return f"{self.name}"


class Grade(models.Model):
    class_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Grade Name",
        help_text="enter name is numberic",
    )

    class Meta:
        db_table = "grade"

    def __str__(self):
        return f"{self.name}"