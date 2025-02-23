from django.db import models

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=20),
#     description = models.TextField(), 
#     price = models.DecimalField(max_length=5) ,
#     category = models.CharField(max_length=8)

class Book(models.Model):
    title = models.CharField(max_length=300)  
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
