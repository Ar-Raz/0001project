from django.contrib import admin
from .models import Category, CategoryVariation, Variation, MainCategory

from products.models import ProductDetail

admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(CategoryVariation)
# admin.site.register(Variation)



# class InlineProductDetail(admin.TabularInline):
#     model = ProductDetail
#     extra = 1


# class VariationAdmin(admin.ModelAdmin):
#     inlines = [InlineProductDetail]
#     list_filter = ('category',)






# admin.site.register(Variation, VariationAdmin)
