from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView 
from .serializers import UserSerialier
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerialier
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerialier
    queryset = User.objects.all()
