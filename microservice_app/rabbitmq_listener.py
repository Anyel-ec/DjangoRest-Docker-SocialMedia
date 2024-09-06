import pika
import json
from django.conf import settings
from microservice_app.services.user_service import UserService
from microservice_app.serializers.user_serializer import UserSerializer

# Obtener conexión RabbitMQ
def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.RABBITMQ_HOST,
        port=settings.RABBITMQ_PORT,
        credentials=credentials
    ))
    return connection

# Publicar mensaje en una cola de RabbitMQ
def publish_message(queue_name, message):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    
    # Declara la cola (durable)
    channel.queue_declare(queue=queue_name, durable=True)
    
    # Publicar el mensaje
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Hacer persistente el mensaje
        )
    )
    
    # Cerrar la conexión
    connection.close()


    
def callback(ch, method, properties, body):
    try:
        # Convertir el mensaje en JSON
        message = json.loads(body)
        print(f"Procesado mensaje de {method.routing_key}: {message}")
        response_message = None

        # Asegúrate de que el mensaje es un diccionario
        if isinstance(message, dict):
            # Procesar el mensaje: obtener todos los usuarios
            if message.get('request') == 'getAllUsers':
                users = UserService.get_all_users()  # Obtener todos los usuarios
                serialized_users = UserSerializer(users, many=True).data
                response_message = json.dumps({'users': serialized_users})

            # Obtener usuario por ID
            elif message.get('request') == 'getUserById':
                user_id = message.get('userId')
                if user_id:
                    user = UserService.get_user(user_id)
                    serialized_user = UserSerializer(user).data
                    response_message = json.dumps({'user': serialized_user})
                else:
                    response_message = json.dumps({"error": "User ID not provided."})
        else:
            # Si el mensaje no es un diccionario, registrar el error
            response_message = json.dumps({"error": "Invalid message format. Expected a dictionary."})

        # Enviar la respuesta a la cola reply_to
        if response_message and properties.reply_to:
            connection = get_rabbitmq_connection()
            channel = connection.channel()
            channel.queue_declare(queue=properties.reply_to, durable=True)
            channel.basic_publish(
                exchange='',
                routing_key=properties.reply_to,
                body=response_message,
                properties=pika.BasicProperties(correlation_id=properties.correlation_id)
            )
            connection.close()

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")


# Iniciar el listener para las colas
def start_listening():
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue='usersQueue', durable=True)
    channel.queue_declare(queue='userByIdQueue', durable=True)

    channel.basic_consume(queue='usersQueue', on_message_callback=callback, auto_ack=False)
    channel.basic_consume(queue='userByIdQueue', on_message_callback=callback, auto_ack=False)

    print('Esperando mensajes...')
    channel.start_consuming()
