from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
class Book:
    def __init__(self,title,author,publication_year):
        self.title:str[200] = title
        self.author:str[100] = author
        self.publication_year:int = publication_year

def hello(request):
    return render(request,'hello.html',{'name':'hamadaa'})

def index(request):
    return HttpResponse("Welcome to my book store.") 