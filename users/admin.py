from django.contrib import admin

from .models import User, Customer, Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")  # Added for search functionality


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("user", "field")
    search_fields = ("user__username", "field")  # Added search by user and field


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "birth")
    search_fields = ("user__username",)  # Added search by username
