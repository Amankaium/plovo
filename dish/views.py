from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Dish
from .serializers import *


class DishListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.order_by('name')         
        dishes_serialized = DishListSerializer(dishes, many=True)        
        return Response(data=dishes_serialized.data)


class DishCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DishCreateSerializer(data=data)
        if serializer.is_valid():
            dish_object = serializer.save()
            return Response(data={'message': 'Блюдо успешно добавлено'}, status=201)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)

        data = request.POST
        serializer = DishUpdateSerializer(data=data)

        if serializer.is_valid():
            dish.name = serializer.validated_data.get('name')
            dish.price = serializer.validated_data.get('price')
            dish.save()
            serialized_object = DishSerializer(dish)
            json_data = serialized_object.data
            return Response(data=json_data)        
        return Response(data=serializer.errors)


class DishDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            dish_object = Dish.objects.get(pk=kwargs.get('pk'))
            serializer = DishSerializer(instance=dish_object)
            return Response(data=serializer.data)
        except Dish.DoesNotExist as e:
            return Response(data=f"{e}", status=status.HTTP_404_NOT_FOUND)


class DishDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        dish = Dish.objects.get(pk=kwargs.get('pk'))
        dish.delete()
        return Response(data={'message': 'Блюдо было удалено'}, status=status.HTTP_204_NO_CONTENT)
