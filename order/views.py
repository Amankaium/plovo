from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        try:
            order = Order.objects.get(pk=kwargs.get('pk'))
        except Order.DoesNotExist as e:
            return Response(data={"message": f'Order was not found: {e}'}, status=404)
        
        serializer = OrderSerializer(instance=order)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs.get('pk'))
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs.get('pk'))
        order.status = 3
        order.save()
        return Response(data={'message': 'Order successfully deleted'})
