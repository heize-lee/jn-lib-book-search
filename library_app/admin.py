from django.contrib import admin
from .models import BookCallNumber

@admin.register(BookCallNumber)
class BookCallNumberAdmin(admin.ModelAdmin):
    list_display = ('call_number', 'title', 'created_at')
