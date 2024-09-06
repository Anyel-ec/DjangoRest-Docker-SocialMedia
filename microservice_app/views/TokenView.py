from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from microservice_app.services.user_service import UserService

class TokenView(viewsets.ViewSet):
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    @action(detail=False, methods=['post'], url_path='token')
    def get_token(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = UserService.verify_password_with_email(email, password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
