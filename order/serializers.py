from rest_framework import serializers
from .models import Order, AdditionDish
from users.serializers import UserSerialier
from dish.serializers import DishListSerializer, DishNameSerializer


class AdditionDishSerializer(serializers.ModelSerializer):
    dish = DishNameSerializer()

    class Meta:
        model = AdditionDish
        fields = ['dish']


class OrderSerializer(serializers.ModelSerializer):
    addition_dish = AdditionDishSerializer(many=True)
    dish = DishNameSerializer()

    class Meta:
        model = Order
        fields = ['dish', 'location', 'phone', 'status', 'email', 'addition_dish']


class OrderDetailSerializer(serializers.ModelSerializer):
    user = UserSerialier()
    addition_dish = AdditionDishSerializer(many=True)

    class Meta:
        model = Order
        exclude = ('discount', 'discount_sum')



