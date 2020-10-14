from django.contrib import admin
from .models import Category, CategoryVariation, Variation, MainCategory, MotherCategory

from products.models import ProductDetail

admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(CategoryVariation)
admin.site.register(Variation)
admin.site.register(MotherCategory)
