import json
import os

from django.contrib.auth import authenticate, login
from django.http import QueryDict
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http.response import HttpResponseBadRequest, HttpResponse, JsonResponse
from website.settings.base import BASE_DIR
from django.core.files.uploadhandler import FileUploadHandler
from django.db.models import Q
# from django.

#COMPONENTS
from products.models import Product, ProductComment
from products.serializers import (
        ProductDetailSerializer, ProductSerializer,
        ProductCommentSerializer
        )

from categories.models import Category, MainCategory
from categories.serializers import CategorySerializer, MainCategorySerializer

from blog.models import  Post
from blog.serializers import PostSerializer

from .forms import SubscriptionForm, DocumentForm, DocumentSerializer
from .models import NewsTellerEmails, Document, AboutUs
from .serializers import AboutUsSerializer

class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/front-end-render.html', {})


class IndexView(View):

    def get(self, *args, **kwargs):
        try:
            products_list = Product.objects.all()

            categories = Category.objects.all()
            categories_ser = CategorySerializer(categories, many=True).data
            categories_ser_json = json.dumps(categories_ser)


            main_categories = MainCategory.objects.all()
            main_categories_ser = MainCategorySerializer(main_categories, many=True).data
            main_categories_ser_json =json.dumps(main_categories_ser)



            posts = Post.objects.all()[:3]
            post_ser = PostSerializer(posts, many=True).data
            post_ser_json = json.dumps(post_ser)

            product_comments = ProductComment.objects.all()[0:10]
            sered_comments = ProductCommentSerializer(product_comments, many=True).data
            json_comments = json.dumps(sered_comments)

            products_ser = ProductDetailSerializer(products_list, many=True).data
            products_ser_json = json.dumps(products_ser)


            new_products = Product.objects.all().order_by('-date_addded')
            sered_new_products = ProductDetailSerializer(new_products, many=True).data
            new_products_json_string =  json.dumps(sered_new_products)

            best_sellers = Product.objects.filter(label='پرفروش')
            sered_best_seller_products = ProductDetailSerializer(best_sellers, many=True).data
            best_sellers_json_string = json.dumps(sered_best_seller_products)


            context = {
                'products' : products_ser_json,
                'categories' : categories_ser_json,
                'main_categories' : main_categories_ser_json,
                'posts' : post_ser_json,
                'new_products' : new_products_json_string,
                'best_sellers' : best_sellers_json_string,
                'comments' : json_comments,
            }
            return render(self.request, "views/index.html", context)
        except ObjectDoesNotExist:
            message = messages.ERROR("سرور ترکیده")
            return HttpResponseBadRequest("Object Does Not Exist")


    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            if request.user.is_authenticated():
                news_teller, created = NewsTellerEmails.objects.get_or_create(
                    user=request.user,
                    email=email
                )
            else:
                news_teller = NewsTellerEmails.objects.create(
                    email=email
                )
            return redirect("/")

        else:
            message = messages.ERROR("لطفا ایمیل معتبر وارد کنید")
            return HttpResponseBadRequest("form")



def test(request):
    if request.method == 'POST':
        files = request.FILES
        single = files.getlist('file')[0]
        file_name = single.name
        document = Document.objects.create(
            name=file_name,
            document=single,
        )
        location = "location"
        path = f"images/documents/{file_name}"
        context = { 'response' : f'{{location: "{path}"}}'}
        json_context = json.dumps(context)
        render(request, 'views/userPanel.html',json_context)
        return HttpResponse('Done')
    return HttpResponse("this is get")



def aboutus(request):
    obj = AboutUs.objects.all()[0]
    sered_qs = AboutUsSerializer(obj).data
    json_about_us_string =json.dumps(sered_qs)

    return render(request, "aboutUs.html",
            { 'aboutUs' : json_about_us_string})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()
        sered_queryset = ProductDetailSerializer(queryset, many=True).data
        json_string = json.dumps(sered_queryset)

        context = {
            'queryset': json_string
        }
        return render(request, 'views/products.html', context)
