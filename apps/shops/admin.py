from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
# https://tretyakov.net/post/drevovidnye-kategorii-v-django/



