from django.urls import path
from .views import (UserListCreateAPIView,
                    UserRetrieveUpdateDestroyAPIView,
                    RegistrationAPIView,
                    )
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('registration/', RegistrationAPIView.as_view(), name='registration')
]