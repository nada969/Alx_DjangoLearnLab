from django.urls import path
from . import views                 ##(.) refere to here


#url configuration:
urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello)
]