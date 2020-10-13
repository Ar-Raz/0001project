from django.urls import path

from . import views

app_name="dad"

urlpatterns = [
    path('', views.IndexView.as_view(), name="admin-index"),
    path('sorry/', views.NotFound404.as_view()),
    path('add/category/', views.CreateCategoryView.as_view(), name="add-category"),
    path('select/main_category/', views.AllCategoriesSelectionView.as_view(), name="select_main"),
    path('select/<id>/categories/', views.CategorySelectView.as_view(), name="select_cat"),
    path('select/<id>/products/', views.ProductsListView.as_view()),
]