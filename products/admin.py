from django.contrib import admin
from . import models

admin.site.register(models.Variation)
admin.site.register(models.ProductVariation)
admin.site.register(models.Rating)
admin.site.register(models.SliderImage)
admin.site.register(models.MetaDetail)
# admin.site.register(models.Product)

# class ProductInline(admin.TabularInline):
#     model = models.ProductDetail.products.through

# class ProductDetailAdmin(admin.ModelAdmin):
#     inlines = [ProductInline]

# admin.site.register(models.ProductDetail, ProductDetailAdmin)