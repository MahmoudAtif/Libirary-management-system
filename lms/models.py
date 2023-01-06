from distutils.command.upload import upload
from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Author(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='authers_images/')

    def __str__(self):
        return self.name

class Book(models.Model):
    
    Status_book=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media')
    pages=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(max_digits=5 ,decimal_places=2, null=True , blank=True)
    rent=models.DecimalField(max_digits=5 , decimal_places=2, null=True , blank=True)
    rent_period=models.DecimalField(max_digits=5 , decimal_places=2, null=True , blank=True)
    price_rent=models.DecimalField(max_digits=5 , decimal_places=2, null=True , blank=True)
    active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,choices=Status_book)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    author = models.ForeignKey("lms.Author", blank=True, null=True, on_delete=models.PROTECT, related_name="books")

    def __str__(self):
        return self.book_name