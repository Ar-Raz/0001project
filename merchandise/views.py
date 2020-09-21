from rest_framework import viewsets, status, permissions, authentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

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
    queryset = MiniOrder.objects.all()

    def perform_create(self, serializer):
        product_name = self.request.data.get('product_name')
        product = Product.objects.get(title=product_name)
        serializer.save(product=product)
    


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
        email = request.POST.get('email', '').strip()
        name = request.POST.get('username', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        content = request.POST.get('extra_discription', '').strip()
        product_name = request.POST.get("product_name", "")

        if product_name and name and phone_number:
            product = Product.objects.get(title=product_name)
            # slug = product.slug
            mini_order = MiniOrder.objects.create(
                product=product,
                email=email,
                name=name,
                phone_number=phone_number,
                extra_discription=content,
            )
            messages.success(request, "درخواست شما ارسال شد")
            return redirect('/')
        else:
            messages.error(request, "فرم را درست وارد کنید ")
            return render(request, "<p>500</p>",{})



# class TestView(View):

#     def get(self, request, *args, **kwargs):

#         return render(request, "products.html", {})
