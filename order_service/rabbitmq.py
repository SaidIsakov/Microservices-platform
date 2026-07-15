import pika


def connect_rabbitmq():
  credentials = pika.PlainCredentials('guest', 'guest')
  parameters = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672, credentials=credentials
  )
  connection = pika.BlockingConnection(parameters)
  channel = connection.channel()

  return channel, connection

def declare_orders_exchange(channel):
  channel.exchange_declare(
      exchange='order_events',
      exchange_type='direct',
      durable=True
  )
