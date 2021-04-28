from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import Order

class OrderListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.POST)
        if serializer.is_valid():
            order_object = serializer.save()
            json_serializer = OrderSerializer(instance=order_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)


class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
