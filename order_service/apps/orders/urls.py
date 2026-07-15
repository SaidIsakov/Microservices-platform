from django.urls import path
from .views import CreateOrderView, PayOrderView

urlpatterns = [
  path('orders/', CreateOrderView.as_view(), name='create-order'),
  path('orders/<uuid:order_id>/pay/', PayOrderView.as_view(), name='pay_order')
]
