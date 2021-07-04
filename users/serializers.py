from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'email']


class RegistrationSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(max_length=255)
    password_2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2',
                  'first_name', 'last_name']