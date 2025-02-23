from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader
# from .models import department , employ , product                 ## import the models
# from django.contrib.auth.models import User
# # from django.core.exceptions import ObjectDoesNotExist


# # try:
# #     # Retrieve a user based on username
# #     user = User.objects.get(username='john')
# # except ObjectDoesNotExist:
# #     # Create a new user
# #     user = User.objects.create_user('john', 'john@example.com', 'password123')

# # from django.views.generic import CreateView

# # class SignUpView(CreateView):
# #     form_class = UserCreationForm
# #     success_url = reverse_lazy('login')
# #     template_name = 'registration/signup.html'


# # Create your views here.
# def list_department(request):

#     d3 = department.objects.order_by('id')

#     # Debugging step: Print queryset in the console
#     print("Departments in DB:", d3)  
#     context = {'department_new': d3}  # Fix key name to match the template
#     return render(request, 'relationship_app/index.html', context)

#     # return HttpResponse('hello')


from .models import Author , Book , Librarian 
from .models import Library
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
def list_data(request):
    books = Book.objects.all()

    return render(request,'relationship_app/list_books.html',{'books':books})

class list_de(TemplateView):
    template_name = 'relationship_app/library_detail.html'
