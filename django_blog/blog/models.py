from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     user_id = models.IntegerField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')      ### to Django’s User model, with a relation to handle multiple posts by a single author.
