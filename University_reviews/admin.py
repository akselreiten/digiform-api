from django.contrib import admin
from .models import UniversityReview

# Register your models here.
@admin.register(UniversityReview)
class ApplicationAdmin(admin.ModelAdmin):
    pass