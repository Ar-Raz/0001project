from django.urls import path, include
from rest_framework.routers import DefaultRouter
from merchandise.views import OrderViewSet, MiniOrderCreateAPIView, MiniOrderCreation

app_name = 'merchandise-api'

router = DefaultRouter()
# router.register('merchandise', OrderViewSet.as_view())

urlpatterns = [
    # path('', include(router.urls)),
    path('ask_price', MiniOrderCreateAPIView.as_view()),
    path("ask", MiniOrderCreation.as_view()),
]