from rest_framework import serializers
from microservice_app.models.Status import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'