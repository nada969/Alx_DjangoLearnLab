from rest_framework import serializers
from .models import Book


#### 1️⃣ Define a serializer 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'