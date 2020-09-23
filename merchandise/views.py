from rest_framework import viewsets, status, permissions, authentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem, MiniOrder
from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    MiniOrderSerializer
    )

from products.models import Product

from django.views import View
from django.contrib import messages

from django.shortcuts import redirect, reverse, render


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny, permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication,]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderItemSerializer(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = (permissions.AllowAny, permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication, ]

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(user=user)

class MiniOrderCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MiniOrderSerializer

    def perform_create(self, serializer):
        product_name = self.request.data.get('product_name')
        product = Product.objects.get(title=product_name)
        serializer.save(product=product)

    def post(self, request, *args, **kwargs):
        name = request.data["username"]
        email = request.data["email"] or None
        product_name =  request.data["product_name"]
        phone_number =  request.data["phone_number"]
        extra_discription =  request.data["extra_discription"] or None
        if phone_number and name and product_name:
            product = Product.objects.get(title=product_name)
            mini_order = MiniOrder.objects.create(
                    product=product,
                    name=name,
                    email=email,
                    phone_number=phone_number,
                    extra_discription=extra_discription,
                )


            return Response({"message" : "درخواست شما با موفقیت ثبت شد"}, status=status.HTTP_201_CREATED)
        return Response({
                "message" : "لطفار فرم را تصحیح کنید"
            }, status=status.HTTP_400_BAD_REQUEST)



class MiniOrderCreation(APIView):

    def post(self, request, format=None):
        email = request.data.get("email")
        approval = request.data.get("approval")
        username = request.data.get("username")

        if email and approval and username:
            order = MiniOrder.objects.create(
                    email=email,
                    approval=approval,
                    username=username,
                )
            order.save()
            return Response({
                    "message" : "درخواست شما با موفقیت ثبت شد"
                },
                 status=status.HTTP_201_CREATED)

        return Response({
                "message" : "فیلد را درست وارد کن"
            },
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##########################################################################################

class MiniOrderView(View):

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', '').strip() or None
        name = request.POST.get('username', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        content = request.POST.get('extra_discription', '').strip() or None
        product_slug = request.POST.get("product_slug", "")
        product = Product.objects.get(slug=product_slug)

        if product_slug and name and phone_number:
            mini_order = MiniOrder.objects.create(
                product=product,
                email=email,
                name=name,
                phone_number=phone_number,
                extra_discription=content,
            )
            messages.success(request, "درخواست شما ارسال شد")
            return redirect(reverse("products:product_detail", kwargs= { "slug" : product_slug}))
        else:
            messages.error(request, "فرم را درست وارد کنید ")
            return redirect(reverse("products:product_detail", kwargs= { "slug" : product_slug}))



# class TestView(View):

#     def get(self, request, *args, **kwargs):

#         return render(request, "products.html", {})
