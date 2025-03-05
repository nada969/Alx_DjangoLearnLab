from django.db import models

# Create your models here.

#PARENT
class Author(models.Model):
    name = models.CharField(max_length=100)           # instance of a Field class

    def __str__(self):
        return self.neme

#CHILD
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')  # Reverse access: author.books.all()
#### OR:
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)                # Reverse access would be: author.book_set.all()
    def __str__(self):
        return self.name , self.department_name


#CHILD
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, db_column='books',related_name='library_name')

    def __str__(self):
        return self.department_name

#CHILD
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library,related_name='Librarian')

    def __str__(self):
        return self.department_name
