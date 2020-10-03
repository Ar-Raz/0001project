from django.urls import path

from categories import views

app_name = 'categories-api'

urlpatterns = [
    path('', views.MainCategoryListView.as_view(), name="main-categories_list"),
    path('sub-categories/<title>/', views.CategoryDetailView.as_view(), name="category_details"),
    path('categories-list/', views.CategoryListView.as_view(), name="categories_list")
]
