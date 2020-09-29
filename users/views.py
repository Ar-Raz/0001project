import json


from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.views import View

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from rest_framework.views import APIView
from rest_framework import  status

from rest_auth.registration import views

from .permissions import IsOwnerOrReadOnly, IsProducer
from .models import ProducerProfile, Profile
from .forms import ProducerProfileForm, CustomerProfileForm
from .serializers import (
            ProducerProfileSerializer,
            ProfileSerializer,
            ProducerProfileDetailSerializer,
            UserSerializer,
            RegisterSerializer,
            LoginSerializer,
)

from users.models import User
from categories.models import MainCategory, Variation, Category
from categories.serializers import (
            MainCategoryQuickSerializer,
            CategoryTitleSerializer,
            MainCategoryTitleSerializer
            )
from products.models import Product, ProductDetail
from products.serializers import (
                ProductDetailSerializer, 
                SimpleProductSerializer
            )   
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

class UserIDView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'userID': request.user.id}, status=status.HTTP_200_OK)


class ProducerProfileRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProducerProfileSerializer
    lookup_field = 'pk'
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, IsProducer)

    def get_queryset(self):
        user = self.request.user
        qs = ProducerProfile.objects.all()
        return qs.filter(user=user)

class ProfileRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    # lookup_field = 'pk'
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        username = self.kwargs['username']
        return Profile.objects.filter(user__username=username)

class ProfileCreateView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated,]
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            profile = Profile.objects.get(user=self.request.user)
            return profile
        except ObjectDoesNotExist:
            return Response({"message": "You do not have an active order"}, status=status.HTTP_400_BAD_REQUEST)



class ProducerProfileCreateView(CreateAPIView):
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsProducer]
    serializer_class = ProducerProfileDetailSerializer
    queryset = ProducerProfile.objects.all()


def sing_up(request):

    return render(request, 'views/signup.html', {})

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

def complete_prod_profile(request):
    producer = ProducerProfile.objects.get(user=request.user)
    form = ProducerProfileForm(instance=producer)
    if request.method == "POST":
        form = ProducerProfileForm(request.POST, instance=producer)
        if form.is_valid():
            gender = json.loads(request.POST['gender'])
            profile_picture = json.loads(request.POST['profile_picture'])
            province = json.loads(request.POST['province'])
            city = json.loads(request.POST['city'])
            company_name = json.loads(request.POST['company_name'])
            phone_number = json.loads(request.POST['phone_number'])
            company_address = json.loads(request.POST['company_address'])
            office_address = json.loads(request.POST['office_address'])
            office_phone_num = json.loads(request.POST['office_phone_num'])
            introduce_yourself = json.loads(request.POST['introduce_yourself'])
            description = json.loads(request.POST['description'])
            web_site = json.loads(request.POST['web_site'])
            categoty = json.loads(request.POST['categoty'])
            department = json.loads(request.POST['department'])
            job_title = json.loads(request.POST['job_title'])
            postal_code = json.loads(request.POST['postal_code'])
            alternative_phone = json.loads(request.POST['alternative_phone'])
            fax_number = json.loads(request.POST['fax_number'])
            business_type = json.loads(request.POST['business_type'])



            return redirect('/products/')
    context = { 'form' : form }
    return render(request, 'complete_prod_prof.html', context)


def customer_profile_completion(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = CustomerProfileForm(instance=profile)
        if request.method == "POST":
            form = CustomerProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('users/profile')
        context = {
            'form': form,
        }
        return render(request, 'complete_customer_profile.html', context)

    except ObjectDoesNotExist:
        return Http404("not found")



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if username and password:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                message = {"messages": "شما با موفقیت وارد شدید"}
                json_message = json.dumps(message)
                return redirect(reverse('pages:index', kwargs=json_message))
            else:
                message = {"messages" : "رمز عبور یا نام کاربری اشتباه است"}
                json_message = json.dumps(message)
                return redirect(reverse('users:login', kwargs=json_message))
        else:
            message = {"messages" : "رمز عبور یا نام کاربری اشتباه است"}
            json_message = json.dumps(message)
            return redirect(reverse('users:login', kwargs=json_message))



def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        user_q = User.objects.filter(username=username)
        email_q = User.objects.filter(email=email)
        if user_q.exists():
            message = {"messages" : "این نام کاربری قبلا ثبت شده است"}
            return redirect('../../accounts/signup/')
        elif email_q.exists():
            message = {"messages" : "این ایمیل قبلا ثبت شده است"}
            return redirect('../../accounts/signup/')
        elif password1 != password2:
            message = {"messages" : "پسورد شما همخوانی ندارد"}
            # render
            return redirect(reverse('../../accounts/signup/'))
        else:
            user = User.objects.create(
                username=username,
                email= email,
                password= password1,
                is_active= True,
                is_staff=False,
                is_superuser=False
            )
            user.save()
            login(request, user)
            return redirect('pages:index')

    return redirect('pages:index')



### User Panel Codes


def create_product_view(request):
    user = request.user
    serialized_user = UserSerializer(request.user).data
    producer = ProducerProfile.objects.get(user=user)
    user_products = Product.objects.filter(producer=producer)
    serialized_products = ProductDetailSerializer(user_products, many=True).data
    json_products = json.dumps(serialized_products)
    json_user_profile_data = json.dumps(serialized_user)

    categories = Category.objects.all()
    sered_cats = CategoryTitleSerializer(categories, many=True).data
    json_cats = json.dumps(sered_cats)

    main_categories = MainCategory.objects.all()
    sered_mains = MainCategoryTitleSerializer(main_categories, many=True).data
    json_mains = json.dumps(sered_mains)

    if request.method == "POST":
        category = request.POST.get("headCategory").strip()
        variations = Variation.objects.filter(category__title=category)
        print(category)
        print(variations)

        product_title = request.POST.get("product-title")
        product_price = request.POST.get("product-price") or None
        product_price2 = request.POST.get("product-price2") or None
        print(request.FILES)
        product_image = request.FILES['product-image']
        files = request.FILES.getlist('slider')
        files_dict = {
            'slider_image1'  : None ,
            'slider_image2' : None,
            'slider_image3' : None,
            'slider_image4' : None,
            'slider_image5' : None,
            'slider_image6' : None,
            'slider_image7' : None,
            'slider_image8' : None,
            'slider_image9' : None,
        }
        for f in range(len(files)):
            files_dict[f"slider_image{f+1}"] = files[f]
        slider_image1 = files_dict['slider_image1']
        slider_image2 = files_dict['slider_image2']
        slider_image3 = files_dict['slider_image3']
        slider_image4 = files_dict['slider_image4']
        slider_image5 = files_dict['slider_image5']
        slider_image6 = files_dict['slider_image6']
        slider_image7 = files_dict['slider_image7']
        slider_image8 = files_dict['slider_image8']
        slider_image9 = files_dict['slider_image9']
        product_description = request.POST.get("product-description") or None
        product_made_in = request.POST.get("product-made-in") or None
        product_packing = request.POST.get("product-packing") or None
        product_origin = request.POST.get("product-origin") or None
        product_delivery = request.POST.get("product-delivery") or None
        product_shipping = request.POST.get("product-shipping") or None
        product_payment_type = request.POST.get("product-payment-type") or None
        product_minimum_order = request.POST.get("product-minimum-order") or None
        product_samples = request.POST.get("product-samples") or None
        product_short_description = request.POST.get("short-description") or None
        if product_title and category and product_image:
            print("got title and category")
            product = Product.objects.create(
                title=product_title,
                price=product_price,
                second_price=product_price2,
                product_image=product_image,
                slider_image=slider_image1,
                slider_image2=slider_image2,
                slider_image3=slider_image3,
                slider_image4=slider_image4,
                slider_image5=slider_image5,
                slider_image6=slider_image6,
                slider_image7=slider_image7,
                slider_image8=slider_image8,
                slider_image9=slider_image9,
                description=product_description,
                minimum_order=product_minimum_order,
                payment_type=product_payment_type,
                packing=product_packing,
                shipping=product_shipping,
                origin=product_origin,
                made_in=product_made_in,
                delivery=product_delivery,
                samples= product_samples,
                short_discription=product_short_description,
                producer=producer,
            )

            for var in variations:
                value = request.POST.get(f"{var.id}")
                if value:
                    try:
                        obj = ProductDetail.objects.get(
                            value=value,
                            variation=var,
                        )
                        obj.products.add(product)
                    except:
                        obj = ProductDetail.objects.create(
                            value=value,
                            variation=var,
                        )
                        obj.products.add(product)
        else:
            messsage = { 'msg' :  "فیلد های ستاره دار نمیتواند خالی باشید "}
            json_msg = json.dumps(messsage)

            context = {
                'cats' : json_cats,
                'user' : json_user_profile_data,
                'msg'  : json_msg,
            }
            print("not good")
            return render(request, "views/userPanel/createProduct.html")

    context = {
        'user': json_user_profile_data,
        'products': json_products,
        'cats' : json_cats,
    }
    return render(request, 'views/userPanel/createProduct.html', context)

class UserPanelView(View):

    def get(self, request, *args, **kwargs):

        user = request.user
        sered_user = UserSerializer(user).data
        json_user = json.dumps(sered_user)

        profile = ProducerProfile.objects.get(user=user)
        sered_profile = ProducerProfileDetailSerializer(profile).data
        json_profile = json.dumps(sered_profile)

        products = Product.objects.filter(producer=profile)
        sered_products = SimpleProductSerializer(products, many=True).data
        json_products = json.dumps(sered_products)

        latest_products = Product.objects.filter()

        return render(request, "template_name", {})



#OTP and 2FacAuth

