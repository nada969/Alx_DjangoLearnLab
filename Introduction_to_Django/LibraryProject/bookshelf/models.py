from django.db import models

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=20),
#     description = models.TextField(), 
#     price = models.DecimalField(max_length=5) ,
#     category = models.CharField(max_length=8)

class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=100),
    publication_year = models.IntegerField()
    
