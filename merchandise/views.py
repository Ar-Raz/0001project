from rest_framework import viewsets, status, permissions, authentication

from .models import Order, OrderItem, MiniOrder
from .serializers import OrderSerializer, OrderItemSerializer

from django.views import View
from django.contrib import messages

from django.shortcuts import redirect, reverse

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
