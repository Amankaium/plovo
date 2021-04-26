from django.urls import path
from .views import DishListAPIView


urlpatterns = [
    path('', DishListAPIView.as_view(), name='dishes'),
]