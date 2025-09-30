from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "amount", "type", "date", "user")
    list_filter = ("type", "date")
    search_fields = ("title", "notes")
