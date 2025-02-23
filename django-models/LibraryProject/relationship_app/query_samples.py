
from .models import Author , Book , Librarian , Library


####Query all books by a specific author.

all_books = Book.objects.order_by('author')

# List all books in a library.
all_book_in_library = Library.objects.filter('books')

# Retrieve the librarian for a library.
all_librarian = Librarian.objects.all()