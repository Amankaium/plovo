from django.urls import path, include
from .views import (UserListCreateAPIView,
                    UserRetrieveUpdateDestroyAPIView, RegistrationAPIView)
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    # path('registr/', RegistrUserView.as_view(), name='registr'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),

]