from django.urls import path

app_name = 'users'

from . import views

urlpatterns = [
    path('profile', views.complete_prod_profile, name="profile"),
    path('customer/profile', views.customer_profile_completion, name="customer-profile"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('product/create/', views.create_product_view),
    path('userspanel/', views.UserPanelView.as_view()),
]