from django.urls import path
from .views import (DishListAPIView,
    DishCreateAPIView, DishDetailAPIView,
    DishUpdateAPIView, DishDeleteAPIView)


urlpatterns = [
    path('', DishListAPIView.as_view(), name='dishes'),
    path('create/', DishCreateAPIView.as_view(), name='create-dish'),
    path('<int:pk>/', DishDetailAPIView.as_view(), name='dish'),
    path('<int:pk>/update/', DishUpdateAPIView.as_view(), name='update-dish'),
    path('<int:pk>/delete/', DishDeleteAPIView.as_view(), name='delete-dish'),
]