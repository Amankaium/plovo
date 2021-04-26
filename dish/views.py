from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Dish
from .serializers import DishListSerializer


class DishListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.order_by('name')         
        dishes_serialized = DishListSerializer(dishes, many=True)        
        return Response(data=dishes_serialized.data)
