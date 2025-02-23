from django.contrib import admin 
from .models import Book

# Customizing the Admin Interface
# @admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')              ## show the details of every book
    search_fields = ('title', 'author', 'publication_year')
    

#  Changing site headings
admin.site.site_header = 'Admin Page'

# Register your models here.
admin.site.register(Book,BookAdmin)  