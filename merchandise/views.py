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

from django.views import View
from django.contrib import messages

from django.shortcuts import redirect, reverse

class MiniOrderCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MiniOrderSerializer
    queryset = MiniOrder.objects.all()

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


class MiniOrderView(View):

    def post(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        content = request.POST.get('content', '').strip()

        if email and name and content:
            mini_order = MiniOrder.objects.create(
                product=product,
                email=email,
                name=name,
                content=content,
            )
            messages.success(request, "درخواست شما ارسال شد")
            return redirect(reverse("products:product_detail", kwargs={'slug': slug}))
        else:
            messages.error(request, "فرم را درست وارد کنید ")
            return redirect(reverse("products:product_detail", kwargs={'slug': slug}))


class MiniOrderCreation(APIView):

    def post(self, request, format=None):
        email = request.POST.get("email", "")
        approval = request.POST.get("approval", "")
        username = request.POST.get("username", "")

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
                serializer.data, status=status.HTTP_201_CREATED)
            
        return Response({
                "message" : "فیلد را درست وارد کن"
            },
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)