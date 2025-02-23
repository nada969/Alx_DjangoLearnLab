from django.db import models

# Create your models here.

#PARENT
class department(models.Model):
    neme = models.CharField(max_length=100)           # instance of a Field class

    def __str__(self):
        return self.neme

#CHILD
class employ(models.Model):
    name = models.CharField(max_length=100)
    department_name = models.ForeignKey(department,on_delete=models.CASCADE, related_name='employess')

    def __str__(self):
        return self.name , self.department_name


#CHILD
class product(models.Model):
    department_name = models.ManyToManyField(department, db_column='department',related_name='products')

    def __str__(self):
        return self.department_name
