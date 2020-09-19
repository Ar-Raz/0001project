from django.urls import path

app_name = 'products'

from . import views

urlpatterns = [
    path('', views.products_list_view, name="products"),
    path('users/', views.user_panel_view, name='userpanel'),
    path("product-detial/<str:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path('<int:page>/', views.paginated_products),
]
