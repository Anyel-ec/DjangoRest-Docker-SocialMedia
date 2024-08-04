from rest_framework.response import Response
from rest_framework import status, viewsets
from ..models import Gender, Province, Status
from microservice_app.serializers.StatusSerializer import StatusSerializer
from ..services import GenderService, ProvinceService, StatusService


class StatusViewSet(viewsets.ViewSet):

    def list(self, request):
        statuses = StatusService.get_all_statuses()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            status = StatusService.create_status(serializer.validated_data)
            return Response(StatusSerializer(status).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        status = StatusService.get_status(pk)
        if status:
            return Response(StatusSerializer(status).data)
        return Response({'message': 'Status not found'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            status = StatusService.update_status(pk, serializer.validated_data)
            return Response(StatusSerializer(status).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        success = StatusService.delete_status(pk)
        if success:
            return Response({'message': 'Status deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'Status not found'}, status=status.HTTP_404_NOT_FOUND)