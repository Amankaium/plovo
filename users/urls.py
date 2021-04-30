from django.urls import path
from .views import (UserListCreateAPIView,
                    UserRetrieveUpdateDestroyAPIView)
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
]