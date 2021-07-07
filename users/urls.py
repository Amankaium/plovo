from django.urls import path, include
from .views import (UserListCreateAPIView,
                    UserRetrieveUpdateDestroyAPIView, RegistrationAPIView,)
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('registr/', RegistrationAPIView.as_view(), name='registr'),
]