from .models import Author , Book , Librarian , Library

####Query all books by a specific author.
def specific_author(author_name):
    author=Author.objects.get(name=author_name)
    all_books=Book.objects.filter(author=author)
    
    return all_books

##### ex:
# author = Author.objects.create('name')
# book1 = Book.objects.create('book1','name')
# book1 = Book.objects.create('book2','name')
# all_books = author.books.all()



# # List all books in a library.
def list_books(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


# # Retrieve the librarian for a library.
def all_librarian(library_name):
    all_librarian = Librarian.objects.get(library=library_name)
    return all_librarian
