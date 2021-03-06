from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerialier, RegistrationSerializer

from django.contrib.auth import get_user_model
# Подключаем статус
from rest_framework import status
# Подключаем компонент для ответа
from rest_framework.response import Response
# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView
# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny
# Подключаем модель User
from .models import User
# Подключаем UserRegistrSerializer
from .serializers import UserRegistrSerializer

User = get_user_model()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerialier
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerialier
    queryset = User.objects.all()





# Создаём класс RegistrUserView

class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_object = RegistrationSerializer(data=request.POST)
        if user_object.is_valid():
            password_1 = user_object.validated_data.get("password_1")
            password_2 = user_object.validated_data.get("password_2")
            if password_1 == password_2:
                user = User()
                user.username = user_object.validated_data.get("username")
                user.email = user_object.validated_data.get("email")
                user.set_password(password_1)
                user.save()
                return Response(data=UserSerialier(user).data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={"error": "Пароли не совпадают"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data=user_object.errors, status=status.HTTP_400_BAD_REQUEST)
