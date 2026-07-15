import pika
from decouple import config

def connect_rabbitmq():
  credentials = pika.PlainCredentials('guest', 'guest')

  host = config('RABBITMQ_HOST', 'rabbitmq')
  port = config('RABBITMQ_PORT', 5672)

  parameters = pika.ConnectionParameters(
    host=str(host),
    port=int(port),
    credentials=credentials
  )
  connection = pika.BlockingConnection(parameters)
  channel = connection.channel()
  return channel, connection

