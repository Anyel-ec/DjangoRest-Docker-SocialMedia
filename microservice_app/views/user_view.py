# views/user_view.py

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from microservice_app.models.user import User
from microservice_app.serializers.user_serializer import UserSerializer
from microservice_app.services.user_service import UserService
from microservice_app.rabbitmq_listener import publish_message
from rest_framework.permissions import IsAuthenticated

import json
class UserView(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            result = UserService.create_user(serializer.validated_data)
            if isinstance(result, dict) and 'error' in result:
                return Response({'message': result['error']}, status=status.HTTP_400_BAD_REQUEST)
            return Response(UserSerializer(result).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = UserService.get_all_users()
        user_data = UserSerializer(users, many=True).data
        publish_message('usersQueue', json.dumps(user_data)) 
        return Response(user_data)


    def retrieve(self, request, pk=None):
        user = UserService.get_user(pk)
        if user:
            user_data = UserSerializer(user).data
            publish_message('userByIdQueue', json.dumps(user_data))
            return Response(user_data)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        user_data = request.data
        updated_user = UserService.update_user(pk, user_data)
        if updated_user:
            return Response(UserSerializer(updated_user).data)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        success = UserService.delete_user(pk)
        if success:
            return Response({'message': 'Usuario eliminado'}, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='verify')
    def verify_password(self, request, pk=None):
        password = request.data.get('password')
        if UserService.verify_password(pk, password):
            return Response({'message': 'Contraseña es correcta'}, status=status.HTTP_200_OK)
        return Response({'message': 'Contraseña es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='verify_login')
    def verify_password_with_email(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if UserService.verify_password_with_email(email, password):
            return Response({'message': 'Contraseña es correcta'}, status=status.HTTP_200_OK)
        return Response({'message': 'Contraseña es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='by_email')
    def get_user_by_email(self, request):
        email = request.query_params.get('email')
        user = UserService.get_user_by_email(email)
        if user:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], url_path='verify_exist')
    def verify_exist_user(self, request):
        email = request.data.get('email')
        if UserService.verify_exist_user(email):
            return Response({'message': 'Usuario existe'}, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['put'], url_path='update_password')
    def update_password(self, request, pk=None):
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        if UserService.verify_password(pk, password):
            user_data = {'password': new_password}
            updated_user = UserService.update_user(pk, user_data)
            return Response(UserSerializer(updated_user).data)
        return Response({'message': 'Contraseña es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
