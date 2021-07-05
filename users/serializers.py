from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

User = get_user_model()

class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username',  'email']




class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()

    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'password2']

    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email=self.validated_data['email'],  # Назначаем Email
            username=self.validated_data['username'],  # Назначаем Логин
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        password2 = self.validated_data['password2']
        # Проверяем совпадают ли пароли
        if password != password2:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(max_length=255)
    password_2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2',
                  'first_name', 'last_name']

