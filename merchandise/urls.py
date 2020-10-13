from django.urls import path

app_name = 'merchandise'

from .views import MiniOrderView

urlpatterns = [
    path('miniorder', MiniOrderView.as_view(), name="miniorder"),
]
