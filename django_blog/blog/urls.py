from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_signup,name='sign_up'),
    path('log_out/',views.user_logout,name='log_out'),
    path('profile/',views.profile,name='profile')
]