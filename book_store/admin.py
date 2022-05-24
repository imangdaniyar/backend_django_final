from django.contrib import admin

# Register your models here.
from book_store.models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'publisher')
