from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "total_amount", "start_date", "end_date", "user")
    list_filter = ("start_date", "end_date")
    search_fields = ("title",)
