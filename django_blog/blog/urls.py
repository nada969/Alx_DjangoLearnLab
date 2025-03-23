from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('sign_up/',views.user_signup,name='sign_up'),
    path('log_out/',views.user_logout,name='log_out')
]