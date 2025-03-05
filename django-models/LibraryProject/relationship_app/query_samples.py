
# from .models import Author , Book , Librarian , Library


# ####Query all books by a specific author.

# all_books = Book.objects.order_by('author')

# # List all books in a library.
# books = Library.objects.get(name=library_name)
# books.all()

# # Retrieve the librarian for a library.
# all_librarian = Librarian.objects.all()

from .models import Author , Book , Librarian , Library


####Query all books by a specific author.
author = Author.objects.create('name')
book1 = Book.objects.create('book1','name')
book1 = Book.objects.create('book2','name')
all_books = author.books.all()


# List all books in a library.
# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.

all_librarian = Librarian.objects.all()
