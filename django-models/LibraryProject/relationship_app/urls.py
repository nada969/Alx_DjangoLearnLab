from django.urls import path
from . import views                 ##(.) refere to here
from .views import list_books

#url configuration:
urlpatterns = [
    path('list_department/', views.list_department) ,
    path('LibraryDetailView/', views.list_department) ,
    path('login/', views.list_department) ,
    path('logout/', views.list_department) ,
    path('register/', views.list_department) 
]
