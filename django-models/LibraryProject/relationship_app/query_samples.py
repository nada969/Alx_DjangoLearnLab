
from .models import Author , Book , Librarian , Library


####Query all books by a specific author.

all_books = Book.objects.order_by('author')

# List all books in a library.
# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.
all_librarian = Librarian.objects.all()
