from django.urls import path

from . import views

urlpatterns = [
    path('newsteller/', views.NewsTellerCreateAPIView.as_view()),
]