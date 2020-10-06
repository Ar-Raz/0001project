from django.urls import path

app_name = "pages"

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('test', views.test),

    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path('about_damir/', views.AboutDamir.as_view(), name='about_damir'),
    path('rules_to_use/', views.RulesToUse.as_view(), name='rules_to_user'),
    path('privacy_policy/', views.Privacy.as_view(), name='privacy'),
    path('buy/', views.BuyFromDamir.as_view(), name="buy_from_damir"),
    path('sell/', views.SearchView.as_view(), name='sell_in_damir'),
]
