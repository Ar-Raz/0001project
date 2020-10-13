# from django.shortcuts import redirect
# from django.contrib import messages
# from django.conf import settings

# def anonymous_required(function=None, redirect_url=None):

#    if not redirect_url:
#        redirect_url = settings.LOGIN_REDIRECT_URL

#    def _inner(request, *args, **kwargs):
#     if request.user.is_authenricated():
#            message = messages.error(request, '{ "message" : "شما از پیش وارد حساب کاربری خود شده اید" }')
#            return redirect("pages:index")
#        return function(request, *args, **kwargs)
#     return _inner


# # def superuser_only(function):

# #     def _inner(request, *args, *kwargs):
# #         if not request.user.is_superuserr:
# #            message = messages.error(request, '{ "message" : "شما اجازه دسرتسی به این صفحه را ندارید  }')
# #            return redirect("pages:index")           
# #         return function(request, *args, **kwargs)
# #     return _inner        

# def producer_only(function):

#     def _inner(request, *args, **kwargs):
#         if not request.user.is_producer:
#            message = messages.error(request, '{ "message" : "شما اجازه دسرتسی به این صفحه را ندارید  }')
#            return redirect("pages:index")           
#         return function(request, *args, **kwargs)
#     return _inner

# def staff_only(function):

#     def _inner(request, *args, **kwargs):
#         if not request.user.is_superuser or request.user.is_staff:
#            message = messages.error(request, '{ "message" : "شما اجازه دسرتسی به این صفحه را ندارید  }')
#            return redirect("pages:index")
#         return function(request, *args, **kwargs)
#     return _inner           
