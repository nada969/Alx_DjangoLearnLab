from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return render(request,'hello.html',{'name':'hamadaa'})

def index(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Welcome to my book store.") 