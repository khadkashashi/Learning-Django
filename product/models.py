from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(max_length=5)

    class Meta:
        db_table = "product"

    def __str__(self):
        return f'{self.name} {self.address}'