from rest_framework import serializers
from microservice_app.models.Province import Province

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
        