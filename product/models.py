##Models are Python classes that represent database tables. Each model attribute represents a database field.
#python manage.py makemigrations to change table name
#then
#python manage.py migrate
#python manage.py showmigrations
#A migration in Django is a way to manage changes in your database structure over time.
#python manage.py shell to write dyango code
#Introduction to Django ORM (Object-RelationaMapping)
##What isORM (Object-Relational Mapping) is a technique that allows you to interact with your #database using Python code instead of writing raw #SQL queries. Django provides its own powerful ORM #that translates Python code into SQL statements #automatically.
# Product.objects.values('name','address')---> to see data post in db
#Product.object.filter(address='addressname').delete()
#Retrieving All Objects-----> #Product.objects.all()
#get_or_create() - Avoid Duplicates---> Category.objects.get_or_create(------)
from django.db import models
# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=100, null=True)
    phone=models.IntegerField()
    class Meta:# to overwrite 
        db_table="hari"
    def __str__(self):
            return f'{self.name}={self.address}'
