from rest_framework import generics
from publisher import send_orders_exchange
from .models import Order
from .serializers import OrderSerializer

class CreateOrderView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

  def perform_create(self, serializer):
    order = serializer.save()

    try:
      send_orders_exchange(order)
    except Exception as e:
      print(f"Ошибка RabbitMQ: {e}")
