from django.urls import path
from . import views                 ##(.) refere to here


#url configuration:
urlpatterns = [
    path('index/', views.index, name="index"),
    path('hello/', views.hello)
]