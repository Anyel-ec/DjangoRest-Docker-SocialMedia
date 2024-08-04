from rest_framework.response import Response
from rest_framework import status, viewsets
from ..models import Gender, Province, Status
from microservice_app.serializers.genderSerializer import GenderSerializer

from ..services import GenderService
class GenderViewSet(viewsets.ViewSet):

    def list(self, request):
        genders = GenderService.get_all_genders()
        serializer = GenderSerializer(genders, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            gender = GenderService.create_gender(serializer.validated_data)
            return Response(GenderSerializer(gender).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        gender = GenderService.get_gender(pk)
        if gender:
            return Response(GenderSerializer(gender).data)
        return Response({'message': 'Gender not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            gender = GenderService.update_gender(pk, serializer.validated_data)
            return Response(GenderSerializer(gender).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        success = GenderService.delete_gender(pk)
        if success:
            return Response({'message': 'Gender deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'Gender not found'}, status=status.HTTP_404_NOT_FOUND)
