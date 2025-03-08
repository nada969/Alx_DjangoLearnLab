from . import views
from django.urls import path
# from views import BookList

#######3️⃣ Register endpoints in urls.py:
urlpatterns = [
    path('books/',views.BookList.as_view(),name='BookList')    # Maps to the BookList view
]