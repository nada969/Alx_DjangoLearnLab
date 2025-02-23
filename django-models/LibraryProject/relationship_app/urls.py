from django.urls import path
from . import views                 ##(.) refere to here


#url configuration:
urlpatterns = [
    path('list_department/', views.list_department) 
]