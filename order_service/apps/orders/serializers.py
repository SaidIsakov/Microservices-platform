from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['id', 'user_email', 'product_name', 'price', 'status', 'created_at',  'user_telegram_id']
    read_only_fields = ['id', 'status', 'created_at']


