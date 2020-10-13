from rest_framework import serializers

from .models import (
            Product,
            ProductVariation,
            Variation,
            ProductComment,
            Rating,
            ProductDetail,
            SliderImage,
            Label,
            )

from users.serializers import UserSerializer,ProducerProfileDetailSerializer
from categories.serializers import CategorySerializer, VariationDetailSerializer


class ProductTechDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = (
            'id',
            'value',
            'variation',
            'products',
        )


class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'product_image',
            'orderd_times',
        )


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

class ProductSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SliderImage
        fields = (
            'id',
            'image',
        )

class ProductDetailSerializer(serializers.ModelSerializer):
    sample = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    sliders = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'second_price',
            'discount_price',
            'slug',
            'stock',
            'description',
            'product_image',
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
            # 'hit_count',
            'sliders',
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

    def get_sliders(self, obj):
        return ProductSliderSerializer(obj.get_sliders, many=True).data







class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'starts', 'user', 'product')



class ProductTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug'
        )

class ProductCommentDetailSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = ProductComment
        fields = (
            'id',
            'is_confirmed',
            'content',
            'user',
            'username',
            'item'
        )

    def get_item(self, obj):
        return ProductTitleSerializer(obj.product).data


class LabeledProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Label 
        fields = (
            'id',
            'title',
            'slug',
            'products',
        )

    def get_products(self, obj):
        products = Product.objects.filter(label_try=obj)
        return ProductSerializer(products, many=True).data


class ProducerPageQuickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'product_image',
            'description',
            # 'hit_count',
        )