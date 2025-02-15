from django.contrib import admin 
from .models import Book


# Customizing the Admin Interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date')

# Register your models here.
admin.site.register(Book,BookAdmin)  
