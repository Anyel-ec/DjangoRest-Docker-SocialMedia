# myapp/management/commands/start_rabbitmq_listener.py

from django.core.management.base import BaseCommand
from microservice_app.rabbitmq_listener import start_listening

class Command(BaseCommand):
    help = 'Starts the RabbitMQ listener for Django'

    def handle(self, *args, **kwargs):
        start_listening()
