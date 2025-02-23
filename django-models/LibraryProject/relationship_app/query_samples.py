
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

all_books = Book.objects.order_by('author')
Author.objects.get(name=author_name)
objects.filter(author=author)

# List all books in a library.
# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.
all_librarian = Librarian.objects.all()
<<<<<<< HEAD
Librarian.objects.get(library=)
=======
Librarian.objects.get(library=)
>>>>>>> 928ea6dca8a0427b25e88ff4a7c7fc74f53d37d1
