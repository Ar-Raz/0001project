from django.contrib import admin
from .models import Product, ProductVariation, Variation, ProductComment, Rating,ProductDetail

admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ProductVariation)
admin.site.register(Rating)
admin.site.register(ProductComment)
admin.site.register(ProductDetail)
