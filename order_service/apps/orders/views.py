from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class CreateOrderView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

  def perform_create(self, serializer):
    # Пока просто сохраняем, позже сюда добавим RabbitMQ
    serializer.save()
