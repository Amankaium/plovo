from rest_framework import serializers

from .models import Dish


class DishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')
    

class DishCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        # fields = ('name', 'price')
        exclude = ['id']


class DishUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'price')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')
