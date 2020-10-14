from django.urls import path

from categories import views
from .views import MotherCategoryAPIView, MainCategoryListAPIView, CategoryListAPIView

app_name = 'categories-api'

urlpatterns = [
    path('', views.MainCategoryListView.as_view(), name="main-categories_list"),
    path('sub-categories/<title>/', views.CategoryDetailView.as_view(), name="category_details"),
    path('categories-list/', views.CategoryListView.as_view(), name="categories_list"),
    path('/variations/<pk>/', views.CategoryListAPIView.as_view()),
    path('/list/', views.QuickCategoriesList.as_view()),

    path('/mother/', MotherCategoryAPIView.as_view()),
    path('/mother/<id>/', MainCategoryListAPIView.as_view()),
    path('/mother/<id>/main/<id2>/', CategoryListAPIView.as_view()),
    path('/mother/<id>/main/<id2>/cat/<pk>/', views.CategoryListAPIView.as_view() ),
]
