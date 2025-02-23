from django.urls import path
from . import views                 ##(.) refere to here
from .views import list_books
LogoutView.as_view(template_name=)
LoginView.as_view(template_name=)
#url configuration:
urlpatterns = [
    path('list_department/', views.list_department) ,
    path('LibraryDetailView/', views.LibraryDetailView) ,
    path('login/', views.login) ,
    path('logout/', views.logout) ,
    path('register/', views.register) 
]
