from django.contrib import admin
from . import models

admin.site.register(models.Variation)
admin.site.register(models.ProductVariation)
admin.site.register(models.Rating)
admin.site.register(models.ProductDetail)
admin.site.register(models.SliderImage)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer')


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_confirmed', 'username')

    def active(self, obj):
        return obj.is_confirmed == 1

    active.boolean = True

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductComment, ProductCommentAdmin)
