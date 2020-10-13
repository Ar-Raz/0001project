from rest_framework import  response, status

import six

from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.shortcuts import redirect

class AnonymousMixin(AccessMixin):

    def handle_no_permission(self):
        # message = messages.success(request, '{ "message" : "شما دسترسی به این صفحه ندارید " }')
        return redirect("pages:index")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ProducerOnlyMixin(AccessMixin):

    def handle_no_permission(self):
        # message = messages.success(request, '{ "message" : "نوع حساب کاربری شما اجازه دسترسی ندارد" }')
        return redirect("users:profile")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_producer:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)