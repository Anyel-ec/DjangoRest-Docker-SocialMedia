"""
WSGI config for microservice_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microservice_project.settings')

application = get_wsgi_application()

# Importa y configura el cliente de Eureka
import py_eureka_client.eureka_client as eureka_client

# Configuración del servidor Eureka y del servicio
EUREKA_SERVER = "http://localhost:8761/eureka"
SERVICE_NAME = "django-service"
SERVICE_PORT = 8000  # Asegúrate de que este sea el puerto en el que tu servicio Django está escuchando

# Registrar el servicio en Eureka
eureka_client.init(eureka_server=EUREKA_SERVER,
                   app_name=SERVICE_NAME,
                   instance_port=SERVICE_PORT)
