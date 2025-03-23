from django.urls import path, include
from . import views
from .views import post_view, create_post, post_delete, post_detail, post_update

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_signup,name='sign_up'),
    path('log_out/',views.user_logout,name='log_out'),
    path('profile/',views.profile,name='profile'),
    path('posts/', post_view.as_view(), name='post'),
    path('"post/new/',create_post.as_view(),name='create_post'),
    path('post/<int:pk>/delete/',post_delete.as_view()) ,
    path("post/<int:pk>/update/",post_update.as_view()),

]"tags/<slug:tag_slug>/", "PostByTagListView.as_view()"
