from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


#### 2️⃣ Create API views
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer