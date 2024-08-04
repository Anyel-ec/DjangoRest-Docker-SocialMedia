from rest_framework.response import Response
from rest_framework import status, viewsets
from microservice_app.models.Province import Province
from microservice_app.serializers.ProvinceSerializer import ProvinceSerializer
from microservice_app.services.ProvinceService import ProvinceService
class ProvinceViewSet(viewsets.ViewSet):

    def list(self, request):
        provinces = ProvinceService.get_all_provinces()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            province = ProvinceService.create_province(serializer.validated_data)
            return Response(ProvinceSerializer(province).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        province = ProvinceService.get_province(pk)
        if province:
            return Response(ProvinceSerializer(province).data)
        return Response({'message': 'Province not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            province = ProvinceService.update_province(pk, serializer.validated_data)
            return Response(ProvinceSerializer(province).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        success = ProvinceService.delete_province(pk)
        if success:
            return Response({'message': 'Province deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'Province not found'}, status=status.HTTP_404_NOT_FOUND)
