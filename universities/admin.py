from django.contrib import admin
from .models import University

# Register your models here.

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass