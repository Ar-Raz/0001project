from django.contrib import admin
from .models import Product, ProductVariation, Variation, ProductComment, Rating,ProductDetail


admin.site.register(Variation)
admin.site.register(ProductVariation)
admin.site.register(Rating)
admin.site.register(ProductDetail)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer')


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_confirmed', 'username')

    def active(self, obj):
        return obj.is_confirmed == 1

    active.boolean = True

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment, ProductCommentAdmin)
