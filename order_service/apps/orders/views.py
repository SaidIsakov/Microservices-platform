from rest_framework.response import Response
from rest_framework import generics
from publisher import send_orders_exchange
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView



class CreateOrderView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

  def perform_create(self, serializer):
    order = serializer.save()

    try:
      send_orders_exchange(order, 'order.created')
    except Exception as e:
      print(f"Ошибка RabbitMQ: {e}")


class PayOrderView(APIView):
  def post(self, request, order_id):
    try:
      order = Order.objects.get(id=order_id)
      order.status = 'PAID'
      order.save()
      send_orders_exchange(order, 'order.paid')
      return Response({'status': 'order paid'}, status=200)
    except Order.DoesNotExist:
      return Response({'status': 'order does not exist'}, status=404)

