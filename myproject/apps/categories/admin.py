from django.contrib import admin
from .models import Category, CategoryTranslations

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryTranslations)
