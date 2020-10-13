from django.urls import path

app_name= 'categories'

from . import views

urlpatterns = [
    path('', views.category_list_view, name="categories-list"),
    path('<name>/', views.by_category, name="by_category"),
    path('create/variation/', views.VariationHandling.as_view(), name='create_var'),
]
