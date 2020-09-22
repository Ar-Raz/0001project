import json

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.response import Response


from .serializers import (
        CategorySerializer,
        CategoryDetailSerializer,
        VariationDetailSerializer,
        MainCategorySerializer
        )
from .models import Category, Variation, CategoryVariation, MainCategory

from products.models import Product
from products.serializers import ProductDetailSerializer

"""
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""


class CategoryListView(ListAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategoryDetailSerializer
    lookup_field = 'title'
    queryset = Category.objects.all()

class MainCategoryListView(ListAPIView):
    serializer_class = MainCategorySerializer
    queryset = MainCategory.objects.all()
"""
END OF:
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################
"""

def category_list_view(request):
    categories = Category.objects.all()
    serialized_data = CategorySerializer(categories, many=True).data
    main_categories = MainCategory.objects.all()
    serialized_main_categories_data = MainCategorySerializer(main_categories, many=True).data
    categories_json_string = json.dumps(serialized_data)
    main_categories_json_string = json.dumps(serialized_main_categories_data)
    context = {
        'categories' : categories_json_string,
        'main_categories' : main_categories_json_string,
    }
    return render(request, 'views/template/header.html', context)

def by_category(request, name):
    category = Category.objects.get(title=name)
    products = Product.objects.filter(category=category)

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 12)
    number_of_pages = paginator.num_pages

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    serialized_products = ProductDetailSerializer(products, many=True).data
    json_products = json.dumps(serialized_products)

    page_data = { "current_page" : page , "number_of_pages" : number_of_pages }
    json_page_data = json.dumps(page_data)

    context = {
        'products' : json_products,
        "page_data" : json_page_data,
    }
    return render(request, 'views/products.html', context)
