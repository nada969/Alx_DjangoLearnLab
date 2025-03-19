from django.db import router
from . import views
from django.urls import path , include
from rest_framework.routers import DefaultRouter 

router.register(r'books_all', BookViewSet.DefaultRouter(), basename='book_all')
#######3️⃣ Register endpoints in urls.py:
urlpatterns = [
    path('books/',views.BookList.as_view(),name='BookList'),    # Maps to the BookList view
    # router.register(r'books_all', BookViewSet, basename='book_all')
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]