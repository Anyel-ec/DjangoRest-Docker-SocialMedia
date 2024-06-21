from microservice_app.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'birthdate', 'password', 'salt']
        extra_kwargs = {
            'password': {'write_only': True},
            'salt': {'write_only': True}
        }