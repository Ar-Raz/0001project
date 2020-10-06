import json
import random

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.views import View
from django.utils import timezone


from website.utils import send_otp_kavenegar
from website.mixins import GroupRequiredMixin

from .models import ProducerProfile, Profile, TokenTFA
from .forms import ProducerProfileForm, CustomerProfileForm
from .serializers import (
    ProducerProfileSerializer,
    ProfileSerializer,
    ProducerProfileDetailSerializer,
    TokenSerializer
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView

from kavenegar import KavenegarAPI

from products.models import Product, ProductDetail, SliderImage
from products.serializers import (
    ProductDetailSerializer,
    SimpleProductSerializer,
    ProductSerializer,
)
from users.models import User
from users.serializers import UserSerializer
from categories.models import MainCategory, Category, Variation
from categories.serializers import (
    CategoryTitleSerializer,
    MainCategoryTitleSerializer
)
from merchandise.serializers import MiniOrderSimpleSerializer, MiniOrderDetailSerializer
from merchandise.models import MiniOrder

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
    context = {'form': form}
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
                message = {"messages": "رمز عبور یا نام کاربری اشتباه است"}
                json_message = json.dumps(message)
                return redirect(reverse('users:login', kwargs=json_message))
        else:
            message = {"messages": "رمز عبور یا نام کاربری اشتباه است"}
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
            message = {"messages": "این نام کاربری قبلا ثبت شده است"}
            return redirect('../../accounts/signup/')
        elif email_q.exists():
            message = {"messages": "این ایمیل قبلا ثبت شده است"}
            return redirect('../../accounts/signup/')
        elif password1 != password2:
            message = {"messages": "پسورد شما همخوانی ندارد"}
            render
            return redirect(reverse('../../accounts/signup/'))
        else:
            user = User.objects.create(
                username=username,
                email=email,
                password=password1,
                is_active=True,
                is_staff=False,
                is_superuser=False
            )
            user.save()
            login(request, user)
            return redirect('pages:index')

    return redirect('pages:index')


# OTP verification

class TwoFactorEntry(View, SuccessMessageMixin):

    def get(self, request, *args, **kwargs):

        return render(request, 'views/signup.html', {})

    def post(self, request, *args, **kwargs):
        phone_number = request.POST.get('phonenumber')
        random_num = random.randint(100000, 999999)
        if phone_number:
            qs = User.objects.filter(phone_number=phone_number)
            if qs.exists():
                user = User.objects.get(phone_number=phone_number)
                token = TokenTFA.objects.get(user=user)
                token.code = random_num
                token.gen_time = timezone.now()
                token.save()
            else:
                user = User.objects.create(
                    username=phone_number,
                    phone_number=phone_number,

                )
                token = TokenTFA.objects.get(user=user)
                token.code = random_num
                token.gen_time = timezone.now()
                token.save()

            params = {
			        "sender": "1000596446",
			        'receptor' : phone_number,
			        'message'  : f"Kavenegar serivice works fine dude you token:{random_num}"
			        }
            # send_otp_kavenegar(params)
            return redirect(reverse('users:verify', kwargs={ 'phone' : phone_number}))
        else:
            request.session['message'] = "لطفا شناره تلفن خود را وارد کنید"
            return redirect('users:tfentry')


class VerifyTF(View):

    def get(self, request, phone, *args, **kwargs):

        return render(request, 'views/confirmation.html', {})

    def post(self, request, phone, *args, **kwargs):
        try:
            token_number = request.POST.get('token-number')
            user = User.objects.get(phone_number=phone)
            token = TokenTFA.objects.get(user=user)
            if token_number:
                if token_number == token.code:
                    now = timezone.now()
                    t_1 = token.gen_time
                    delta = now - t_1
                    if delta.seconds <= 150:
                        login(request, user=user)
                        return redirect("pages:index")
                    else:
                        request.session['message'] = 'کد شما منقضی شده یکبار دیگر تلاش گنید'
                        return redirect('users:tfentry')
                else:
                    request.session['message'] = 'کد تایید مطابقت ندارد یکبار دیگر تلاش کنید'
                    return redirect('users:tfentry')
            else:
                request.session['message'] = 'کد تایید را وارد کنید'
                return redirect(reverse('user:verify', kwargs={'phone':phone}))
        except ObjectDoesNotExist:
            request.session['message'] = 'خطای سرور'
            return redirect('users:tfentry')

# OTP done
# def send_otp():




# User Panel Codes
# Producer


def create_product_view(request):
    # body = json.loads(body_unicode)
    # content = body['content']
    # print(content)
    # print(body)
    user = request.user
    # user = User.objects.get(username='jer')
    serialized_user = UserSerializer(user).data
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
        cat = Category.objects.get(title=category)
        variations = Variation.objects.filter(category__title=category)

        product_title = request.POST.get("product-title")
        product_price = request.POST.get("product-price") or None
        product_price2 = request.POST.get("product-price2") or None
        product_image = request.FILES['product-image']
        files = request.FILES.getlist('slider')
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
                producer_id=user.id,
                title=product_title,
                price=product_price,
                second_price=product_price2,
                product_image=product_image,
                description=product_description,
                minimum_order=product_minimum_order,
                payment_type=product_payment_type,
                packing=product_packing,
                shipping=product_shipping,
                origin=product_origin,
                made_in=product_made_in,
                delivery=product_delivery,
                samples=product_samples,
                short_discription=product_short_description,
            )
            product.producer = producer
            product.category.add(cat)
            product.save()

            for f in files:
                slider_image = SliderImage.objects.create(
                    product=product,
                    image=f
                )

            for var in variations:
                value = request.POST.get(f"{var.id}")
                if value:
                    qs = ProductDetail.objects.filter(
                        value=value,
                        variation=var
                    )
                    if qs.exists():
                        obj = ProductDetail.objects.get(
                            value=value,
                            variation=var,
                        )
                        obj.products.add(product)
                    else:
                        obj = ProductDetail.objects.create(
                            value=value,
                            variation=var
                        )
                        obj.products.add(product)

                    # try:
                    #     obj = ProductDetail.objects.get(
                    #         value=value,
                    #         variation=var,
                    #     )
                    #     obj.products.add(product)
                    # except ObjectDoesNotExist:
                    #     obj = ProductDetail.objects.create(
                    #         value=value,
                    #         variation=var,
                    #     )
                    #     obj.products.add(product)
        else:
            messsage = {'msg': "فیلد های ستاره دار نمیتواند خالی باشید "}
            json_msg = json.dumps(messsage)

            context = {
                'cats': json_cats,
                'user': json_user_profile_data,
                'msg': json_msg,
            }
            print("not good")
            return HttpResponse("DEAD")

    context = {
        'user': json_user_profile_data,
        'products': json_products,
        'cats': json_cats,
    }
    return render(request, 'views/userPanel/createProduct.html', context)

class ProductEditView(View):

    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        sered_product = ProductSerializer(product).data
        json_product = json.dumps(sered_product)

        context =  {
            'product' : json_product,
        }
        return render(request, 'views/userPanel/createProduct.html', context)

    # def post(self, request, slug, *args, **kwargs):


class ProfileEditView(View):

    def get(self, request, *args, **kwargs):
        request.session['message'] = "user panel here"
        request.COOKIES['message'] = 'sfseg'
        try:
            user = request.user
            sered_user = UserSerializer(user).data
            json_user = json.dumps(sered_user)

            profile = ProducerProfile.objects.get(user=user)
            sered_profile = ProducerProfileDetailSerializer(profile).data
            json_profile = json.dumps(sered_profile)

            context = {
                'profile' : json_profile,
            }

            return render(request, "views/profile.html", context)

        except ObjectDoesNotExist:

            request.session['message'] = "INTERNAL SERVER ERROR"
            return redirect('pages:index')


    def post(self, request, *args, **kwargs):
        profile = ProducerProfile.objects.get(user=request.user)
        user = request.user

        username = request.POST.get("username") or None
        first_name = request.POST.get('firstname') or None
        last_name = request.POST.get('lastname') or None
        gender = request.POST.get('gender') or None
        profile_picture = request.FILES['profile-picture'] or None
        city = request.POST.get('city') or None
        province = request.POST.get('province') or None
        company_name = request.POST.get('compony-name') or None
        phone_number = request.POST.get('phone-number') or None
        office_phone = request.POST.get("office-phone") or None
        office_address = request.POST.get("office-address") or None
        company_address = request.POST.get("compony-adress") or None
        introduction = request.POST.get("introductio") or None
        description = request.POST.get("description") or None
        web_site = request.POST.get("web-site") or None
        department = request.POST.get("department") or None
        job_title = request.POST.get("job-title") or None
        postal_code = request.POST.get("postal-code") or None
        fax_number = request.POST.get("fax-num") or None
        alternative_phone = request.POST.get("alt-phone") or None
        bussiness_type = request.POST.get("bussiness-type") or None

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        # if gender == "آقای":
        #     profile.gender = 'آقای'
        # elif gender == 'خانم':
        #     profile.gender = 'خانم'
        profile.gender = gender
        profile.profile_picture = profile_picture
        profile.province = province
        profile.city = city
        profile.company_name = company_name
        profile.phone_number = phone_number
        profile.office_phone_num = office_phone
        profile.company_address = company_address
        profile.office_address = office_address
        profile.introduce_yourself = introduction
        profile.description = description
        profile.web_site = web_site
        profile.department = department
        profile.job_title = job_title
        profile.fax_number = fax_number
        profile.postal_code = postal_code
        profile.alternative_phone = alternative_phone
        profile.bussiness_type = bussiness_type
        profile.postal_code = postal_code
        profile.save()

        request.session['message'] = 'you ahvee asdacanges suc'

        #message
        return redirect('users:profile')


class UserPanelOverView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = ProducerProfile.objects.get(user=user)
        sered_profile = ProducerProfileDetailSerializer(profile).data
        json_profile = json.dumps(sered_profile)

        products = Product.objects.filter(producer=profile)
        sered_products = SimpleProductSerializer(products, many=True).data
        json_products = json.dumps(sered_products)

        miniorders = MiniOrder.objects.filter(product__producer=profile)
        sered_miniorders = MiniOrderSimpleSerializer(miniorders, many=True).data
        json_orders = json.dumps(sered_miniorders)


        context = {
            'profile' : json_profile,
            'products' : json_products,
            'orders' :  json_orders,
        }

        return render(request, 'path/to/profile/template', context)

class MiniOrderListDetailView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = ProducerProfile.objects.get(user=user)
        miniorders = MiniOrder.objects.filter(product__producer=profile)
        sered_orders = MiniOrderDetailSerializer(miniorders, many=True).data
        json_orders = json.dumps(sered_orders)

        context = {
            'orders' : miniorders
        }

        return render(request, 'orders.html', context)

class Test(View, GroupRequiredMixin):

    group_required = 'producer'
    redirect_field_name = 'pages:index'

    def get(self, request, *args, **kwargs):

        return render(request, 'tess.html', {})
