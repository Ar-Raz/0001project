from rest_framework import serializers

from .models import Product, ProductVariation, Variation , ProductComment, Rating, ProductDetail

from users.serializers import UserSerializer,ProducerProfileDetailSerializer
from categories.serializers import CategorySerializer, VariationDetailSerializer

class ProductDetailsSerializer(serializers.ModelSerializer):
    variation = serializers.SerializerMethodField()

    class Meta:
        model = ProductDetail
        fields = (
            'id',
            'value',
            'attachment',
            'selectable',
            'yes_or_no',
            'variation',
        )

    def get_variation(self, obj):
        return VariationDetailSerializer(obj.variation).data

class ProductSerializer(serializers.ModelSerializer):
    sample = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'second_price',
            'discount_price',
            'product_image',
            'slug',
            'stock',
            'description',
            'minimum_order',
            'payment_type',
            'packing',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'sample',
            'remarks',
            'date_addded',
            'orderd_times',
        )

    def get_sample(self, obj):
        return obj.get_samples_display()

class ProductCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductComment
        fields = (
            'id',
            'is_confirmed',
            'content',
            'user',
            'product',
            'username',
        )



class ProductDetailSerializer(serializers.ModelSerializer):
    sample = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'second_price',
            'discount_price',
            'product_image',
            'slug',
            'stock',
            'description',
            'minimum_order',
            'payment_type',
            'packing',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'sample',
            'remarks',
            'category',
            'average_rating',
            'comments',
            'user',
            'label',
            'detail',
            'date_addded',
            'orderd_times',
        )

    def get_sample(self, obj):
        return obj.get_samples_display()

    def get_category(self, obj):
        return CategorySerializer(obj.category.all(), many=True).data

    def get_user(self, obj):
        return ProducerProfileDetailSerializer(obj.producer).data

    def get_label(self, obj):
        return obj.get_label_display()

    def get_detail(self, obj):
        return ProductDetailsSerializer(obj.productdetail_set.all(), many=True).data

    def get_comments(self, obj):
        return ProductCommentSerializer(obj.get_comments, many=True).data







class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'starts', 'user', 'product')


#
# class ProductDetailSerializer(serializers.ModelSerializer):
#     comments = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Product
#         fields = (
#             'title',
#             'price',
#             'discount_price',
#             'product_image',
#             'slug',
#             'stock',
#             'description',
#             'minimum_order',
#             'payment_type',
#             'packing',
#             'shipping',
#             'origin',
#             'made_in',
#             'delivery',
#             'samples',
#             'remarks',
#             'category',
#             'average_rating',
#             'producer',
#             'comments',
#         )
#         read_only_fields = [ 'producer' ,]
#
#     def get_comments(self, obj):
#         return ProductCommentSerializer(obj.productcomment_set.all(), many=True).data
