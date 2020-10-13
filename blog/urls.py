from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.post_list_view),
    path('posts/', views.post_list),
    path('post/<slug>', views.post_detail, name="post-detail"),
    path("posts/<name>", views.post_by_category),
]
