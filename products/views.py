import json

from rest_framework import viewsets, status, generics, mixins
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from hitcount.views import HitCountMixin, HitCountDetailView
from hitcount.models import HitCount

from .forms import ProductCommentForm
from .models import Product, ProductComment, Rating
from .serializers import ProductSerializer, ProductDetailSerializer, ProductCommentSerializer
from .permissions import IsProducer, IsOwnerOrReadOnly
from .serializers import (ProductSerializer,
            ProductCommentSerializer,
            ProductDetailSerializer,
            RatingSerializer,
            ProductSerializer,
            )


from categories.serializers import (
        MainCategorySerializer,
        CategoryDetailSerializer,
        )
from categories.models import Category, MainCategory
from users.serializers import UserSerializer
from users.models import ProducerProfile
from blog.models import Post
from blog.serializers import PostDetailSerializer
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
class ProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsProducer    )
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProducersProductListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductDetailSerializer

    def get_queryset(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset

class ProducerProductPublicListView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ProductSerializer

    def get_queryset(self):
        company = self.kwargs['company_name']
        return Product.objects.filter(producer__company_name=company)


class ProductCreationView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


    def perform_create(self, serializer):
        producer = ProducerProfile.objects.get(user=self.request.user)
        serializer.save(producer=producer)




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        # 'comments' : reverse('product-comments', request=request, format=format)
    })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=True)
    def rate_product(self, request, pk=None):
        if 'stars' in request.data:
            product = Product.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rating = Rating.objects.get(user=user.id, product=product.id)
                rating.stars = stars
                rating.save()

                serializer = RatingSerializer(rating, many=True)
                response = {'message': 'rating has been updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, product=product, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {'message': 'Please enter stars for the rating'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def comment_on_product(self, request, pk=None, name=None):
        if 'content' in request.data:
            product = Product.objects.get(id=pk, title=name)
            content = request.data['content']
            user = request.user
            try:
                comment = ProductComment.objects.get(user=user.id, product=product.id, is_confirmed=True)
                comment.content = content
                comment.is_confirmed = False
                comment.save()

                serializer = ProductCommentSerializer(comment, many=True)
                response = {"message" : "comment edited wait for the team to revise it",
                            "result" : serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)

            except:
                comment = ProductComment.objects.create(user=user, product=product,
                                                        content=content , is_confirmed=False)
                serializer = ProductCommentSerializer(comment, many=False)
                response = {"message" : "comment posted wait for our to team to review it",
                            'result' : serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            responser = {'message' : 'please fill the required fields' }
            return Response(responser, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(producer=self.request.user)


class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Product.objects.all()

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = Product.objects.all()
    categorise = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_or_category_query = request.GET.get('title_or_category')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    category = request.GET.get('category')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(title_or_category_query):
        qs = qs.filter(Q(title__icontains=title_or_category_query)
                       | Q(category__title__icontains=title_or_category_query)
                       ).distinct()

    if is_valid_queryparam(price_min):
        qs = qs.filter(price__gte=price_min)

    if is_valid_queryparam(price_max):
        qs = qs.filter(price__lt=price_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__title=category)

    return qs


class VueFilterView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        qs = filter(self.request)
        return qs
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

def products_list_view(request):
    queryset = Product.objects.all()

    new_products = queryset.order_by('-date_addded')
    sered_new_products = ProductSerializer(new_products, many=True).data
    new_products_json_string =  json.dumps(sered_new_products)

    best_sellers = Product.objects.filter(label='پرفروش')
    sered_best_seller_products = ProductSerializer(best_sellers, many=True).data
    best_sellers_json_string = json.dumps(sered_best_seller_products)

    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 12)
    number_of_pages = paginator.num_pages

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    sered_data = ProductSerializer(queryset, many=True).data
    json_string = json.dumps(sered_data)



    page_data = { "current_page" : page , "number_of_pages" : number_of_pages }
    json_page_data = json.dumps(page_data)



    context = {
        'products': json_string,
        'new_products': new_products_json_string,
        'best_sellers': best_sellers_json_string,
        'pagination': json_page_data,
    }

    return render(request, 'views/products.html', context)


class ProductDetailView(View, HitCountMixin):
    form = ProductCommentForm()


    def get(self, request, slug, *args, **kwargs):
        try:
            form = ProductCommentForm
            queryset = Product.objects.get(slug=slug)
            serialized_q_set = ProductDetailSerializer(queryset).data
            hit_count = HitCount.objects.get_for_object(queryset)
            hit_count_response = HitCountMixin.hit_count(request, hit_count)
            json_product = json.dumps(serialized_q_set)

            cat = queryset.category.distinct()[0].title
            posts = Post.objects.filter(categories__title=cat)
            sered_posts = PostDetailSerializer(posts, many=True).data
            json_posts = json.dumps(sered_posts)

            related_products = Product.objects.filter(category__title=cat)
            sered_related = ProductSerializer(related_products, many=True).data
            json_related = json.dumps(sered_related)



            context = {
                'product': json_product,
                'object' : queryset,
                'posts' : json_posts,
                'related_products' : json_related,
            }
            return render(request, 'views/product.html', context)
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        content = request.POST.get('content', '').strip()
        username = request.POST.get('username', '').strip()
        serialized_q_set = ProductDetailSerializer(product).data
        json_product = json.dumps(serialized_q_set)
        if username and content:
            comment = ProductComment.objects.create(
                product=product,
                content=content,
                is_confirmed=False,
                username=username,
            )
            comment.save()
            message = messages.success(request, '{ "message" : "نظر شما با موفقیت ثبت شد و در انتظار بررسی است"}')
            return redirect(reverse("products:product_detail",
                                    kwargs={
                                        "slug" : slug
                                    }))
        else:
            message = messages.error(request, '{"message" : "نام کاربری و متن نظر برای ثبت آن لازم است" }')
            return redirect(reverse("products:product_detail",
                                    kwargs={
                                        "slug": slug
                                    }))

        # form = ProductCommentForm(request.POST or None)
        # if form.is_valid():
        #     product = Product.objects.get(slug=slug)
        #     if request.user.is_authenticated():
        #         form.instance.user = self.request.user
        #     form.instance.product = product
        #     form.instance.content = json.loads(request.POST['content'])
        #     form.instance.username = json.loads(request.POST['username'])
        #     # form.instance.content = request.POST['content']
        #     form.save()
        #     return redirect(reverse("products:product_detail", kwargs={'slug': slug}))


def product_detail_view(request, slug):
    product = Product.objects.get(slug=slug)
    sered_data = ProductDetailSerializer(product).data
    json_string = json.dumps(sered_data)
    return render(request, 'views/product.html', {'product': json_string})

def user_panel_view(request):
    serialized_user = UserSerializer(request.user).data
    producer = ProducerProfile.objects.get(user=request.user)
    user_products = Product.objects.filter(producer=producer)
    serialized_products = ProductDetailSerializer(user_products, many=True).data
    json_products = json.dumps(serialized_products)
    json_user_profile_data = json.dumps(serialized_user)
    context = {
        'user': json_user_profile_data,
        'products': json_products,
    }
    return render(request, 'views/userPanel.html', context)




# def paginated_products(request):
#
#     products = Product.objects.all()
#     products_quantity = products.count()
#     number_of_pages = products_quantity/12
#     page = request.GET.get("page","number")
#     current_page = int(page)
#     next_page = int(page) + 1
#     previous_page = int(page) - 1
#     current_page_products = products[(current_page-1)*12 : current_page*12]
#     sered_product = ProductDetailSerializer(current_page_products, many=True).data
#     json_product_string = json.dumps(sered_product)
#
#     page_data = { "current_page" : current_page, "number_of_pages" : number_of_pages }
#     json_page_data = json.dumps(page_data)
#
#     context = {
#         "products" : current_page_products,
#         "pagination" : json_page_data,
#     }
#     return render(request, 'products.html', context)
