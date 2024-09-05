import pika
from django.conf import settings

def callback(ch, method, properties, body):
    print(f"Received message from {method.routing_key}: {body.decode()}")
    # Aquí puedes procesar el mensaje

def start_listening():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST, port=settings.RABBITMQ_PORT)
    )
    channel = connection.channel()

    # Escuchar en la cola usersQueue
    channel.queue_declare(queue='usersQueue', durable=True)
    channel.basic_consume(queue='usersQueue', on_message_callback=callback, auto_ack=True)

    # Escuchar en la cola userByIdQueue
    channel.queue_declare(queue='userByIdQueue', durable=True)
    channel.basic_consume(queue='userByIdQueue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages...')
    channel.start_consuming()
