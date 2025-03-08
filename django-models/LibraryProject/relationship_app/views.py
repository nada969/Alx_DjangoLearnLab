from django.http import HttpResponse
from django.shortcuts import render
from .models import Author , Book , Librarian 
from .models import Library
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

def list_data(request):
    books = Book.objects.all()
    return render(request,'relationship_app/list_books.html',{'books':books})

class list_de(TemplateView):
    template_name = 'relationship_app/library_detail.html'
    
    def list(request):
        return render(request,'relationship_app/register.html',{'books':books , 'library ':library})

