import json

from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.contrib import messages
from django.core.serializers import serialize

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.response import Response


from .serializers import (
        CategorySerializer,
        CategoryDetailSerializer,
        VariationDetailSerializer,
        MainCategorySerializer,
        VarationCreatSerializer,
        MainCategoryQuickSerializer,
        MainCategoryStringSerializer,
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

class QuickCategoriesList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MainCategoryQuickSerializer
    queryset = MainCategory.objects.all()

class CategoryListAPIView(ListAPIView):
    serializer_class = VarationCreatSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        category = Category.objects.get(pk=pk)
        variations = Variation.objects.filter(category=category)
        return variations

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



class VariationHandling(View):
    from django.contrib import messages

    def get(self, request, *args, **kwargs):
        main_cats = MainCategory.objects.all()
        sered_mains = MainCategorySerializer(main_cats, many=True).data
        json_mains = json.dumps(sered_mains)
        
        return render(request, 'views/userpanel/addCat.html',  {'main' : json_mains} )

    def post(self, request, *args, **kwargs):
        main_category_name = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        var_type = request.POST.get('type')
        main_cat = MainCategory.objects.get(title=main_category_name)
        var_names = request.POST.getlist('variation')

        if main_category_name and subcategory:
            qs = Category.objects.filter(title=subcategory)
            if qs.exists():
                category = Category.objects.get(title=subcategory)
            else:
                category = Category.objects.create(
                    title=subcategory,
                    sub_category_of=main_cat,
                    seo_post="NONE YET"
                )
                category.save()

            already_exist = []
            for var_name in var_names:
                qs = Variation.objects.filter(name=var_name, category=category)
                if qs.exists():
                    already_exist.append(var_name)
                else:
                    variation = Variation.objects.create(
                        name=var_name,
                        category=category,
                    )
            try:
                from django.contrib import messages
                if already_exist[0]:
                    insts = ""
                    for inst in already_exist:
                        insts + "," + str(inst)
                    message = messages.success(request, '{ "message" : ":مشخصات وارد شده از پیش موجود است"}')
                    return redirect("categories:create_var")
            except IndexError:
                from django.contrib import messages
                message = messages.success(request, '{ "message" : "مشخصات فنی با موفقیت وارد شد"}')
                return redirect('users:create_product')
        else:
            from django.contrib import messages
            messages = messages.error(request,  '{ "message" : "فیلد های دسته و زیردسته نمیتواند خالی باشد"}')
            return redirect("categories:create_var")





