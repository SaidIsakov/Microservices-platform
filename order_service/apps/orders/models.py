from django.db import models
import uuid


class Order(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user_email = models.EmailField(max_length=50, blank=True, null=True)
  user_telegram_id = models.CharField(max_length=50, blank=True, null=True)
  product_name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=50, default='PENDING')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Order {self.id} - {self.product_name}"
