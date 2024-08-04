
from rest_framework import serializers
from microservice_app.models.Gender import Gender

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'