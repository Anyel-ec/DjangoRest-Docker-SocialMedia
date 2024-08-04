# serializers/user_serializer.py

from rest_framework import serializers
from microservice_app.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'birthdate', 'password', 'province', 'gender', 'status']
        extra_kwargs = {
            'password': {'write_only': True},
            'salt': {'write_only': True}
        }
