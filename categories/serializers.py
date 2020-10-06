from rest_framework import serializers
from .models import Category, CategoryVariation, Variation, MainCategory

class MainCategoryTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCategory
        fields = (
            'id',
            'title',
            'slug',
        )

class CategoryTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
        )

class MainCategoryQuickSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = MainCategory
        fields = (
            'id',
            'title',
            'slug',
            'categories',
        )

    def get_categories(self, obj):
        categories = Category.objects.filter(sub_category_of=obj)
        return CategoryTitleSerializer(categories, many=True).data


class MainCategoryStringSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCategory
        fields = (
            'id',
            'title',
            'seo_post',
            'slug',
        )


class MainCategorySerializer(serializers.ModelSerializer):
    subs = serializers.SerializerMethodField()

    class Meta:
        model = MainCategory
        fields = (
            'id',
            'title',
            'subs',
            'seo_post',
            'slug',
        )

    def get_subs(self, obj):
        categories = Category.objects.filter(sub_category_of=obj)
        return CategoryDetailSerializer(categories, many=True).data

class CategoryStringSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'seo_post',
            'slug',
        )

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'seo_post',
            'slug',
            'sub_category_of',
        )

class VariationDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'category',
        )

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

class CategoryVariationDetailSerializer(serializers.ModelSerializer):
    variation = serializers.SerializerMethodField()

    class Meta:
        model = CategoryVariation
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

class CategoryVariationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryVariation
        fields = (
            'id',
            'variation',
            'value',
            'attachment',
            'selectable',
            'yes_or_no',
        )



class VariationSerializer(serializers.ModelSerializer):
    category_variation = serializers.SerializerMethodField()

    class Meta:
        model = Variation
        fields = (
            'id',
            'name',
            'category_variation',

        )

    def get_category_variation(self, obj):
        return CategoryVariationSerializer(obj.categoryvariation_set.all(), many=True).data


class CategoryDetailSerializer(serializers.ModelSerializer):
    variation = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'variation',
        )

    def get_variation(self, obj):
        return VariationSerializer(obj.variation_set.all(), many=True).data

class MainCategoryQuickSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = MainCategory
        fields = (
            'id',
            'title',
            'slug',
            'categories',
        )

    def get_categories(self, obj):
        categories = Category.objects.filter(sub_category_of=obj)
        return CategoryTitleSerializer(categories, many=True).data

class VarationCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variation
        fields = "__all__"