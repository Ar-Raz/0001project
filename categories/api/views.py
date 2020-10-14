from rest_framework import views, status, generics

from categories.serializers import (
    MotherCategoryQuickSerializer,
    MainCategoryIdSerializer,
    CategoryIdSerializer,
)

from categories.models import (
    MotherCategory,
    MainCategory,
    Category,
)

class MotherCategoryAPIView(generics.ListAPIView):
    serializer_class = MotherCategoryQuickSerializer
    queryset = MotherCategory.objects.all()

class MainCategoryListAPIView(generics.ListAPIView):
    serializer_class = MainCategoryIdSerializer
    
    def get_queryset(self):
        pk = self.kwargs['id']
        queryset = MainCategory.objects.filter(mother_category__id=pk)
        return queryset

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryIdSerializer

    def get_queryset(self):
        pk = self.kwargs['id2']
        queryset = Category.objects.filter(sub_category_of__id=pk)
        return queryset

