from .models import Book

# Create a Book instance
book = Book.objects.create(title='Django Basics', author='John Doe', published_date='2025-02-15') <!-- expected output -->

# Retrieve all products
all_books = Book.objects.all()

# updated title
update_book = Books.objects.update(title=“Nineteen Eighty-Four” if published_date==“1984”)

# Delete
book.delete()
Book.objects.all()