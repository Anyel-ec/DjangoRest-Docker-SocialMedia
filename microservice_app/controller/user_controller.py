from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from microservice_app.serializers.user_serializer import UserSerializer
from microservice_app.services.user_service import UserService


class UserController(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = UserService.create_user(serializer.validated_data)
            return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id=None):
        if user_id:
            user = UserService.get_user(user_id)
            if user:
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = UserService.get_all_users()
            return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user_data = request.data
        updated_user = UserService.update_user(user_id, user_data)
        if updated_user:
            return Response(UserSerializer(updated_user).data, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        success = UserService.delete_user(user_id)
        if success:
            return Response({'message': 'User deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def verify_password(request, user_id):
        password = request.data.get('password')
        if UserService.verify_password(user_id, password):
            return Response({'message': 'Password is correct'}, status=status.HTTP_200_OK)
        return Response({'message': 'Password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def verify_password_with_email(request):
        email = request.data.get('email')
        password = request.data.get('password')
        if UserService.verify_password_with_email(email, password):
            return Response({'message': 'Password is correct'}, status=status.HTTP_200_OK)
        return Response({'message': 'Password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_user_by_email(request):
        email = request.query_params.get('email')
        user = UserService.get_user_by_email(email)
        if user:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def verify_exist_user(request):
        email = request.data.get('email')
        if UserService.verify_exist_user(email):
            return Response({'message': 'User exists'}, status=status.HTTP_200_OK)
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)