from django.urls import path

app_name = 'users'

from . import views

urlpatterns = [
    path('customer/profile/', views.customer_profile_completion, name="customer-profile"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('profile/product/create/', views.create_product_view, name="create_product"),
    path('userpanel/', views.ProfileEditView.as_view()),
    path('entry/', views.TwoFactorEntry.as_view(), name="tfentry"),
    path('tfauth/<phone>/', views.VerifyTF.as_view(), name='verify'),
    path('profile/userpanl/', views.UserProfile.as_view(), name="userpanel"),
    path('profile/', views.UserPanelOverView.as_view(), name='profile'),
    path('profile/orders/', views.MiniOrderListDetailView.as_view(), name='profile-orders'),
    path('profile/my_products/', views.MyProductView.as_view(), name="my_products"),
    path('profile/my_products/<id>/edit/', views.MyProductEditView.as_view(), name='product_edit'),
]
