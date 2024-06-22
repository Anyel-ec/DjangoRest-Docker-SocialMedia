from rest_framework.response import Response
from microservice_app.models.category import Category
from microservice_app.serializers.category_serializer import CategorySerializer
from rest_framework import status, viewsets

from microservice_app.services.category_service import CategoryService


class CategoryView(viewsets.ViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = CategoryService.create_category(serializer.validated_data)
            return Response(CategorySerializer(new_category).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        categories = CategoryService.get_all_categories()
        return Response(CategorySerializer(categories, many=True).data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        category = CategoryService.get_category(pk)
        if category:
            return Response(CategorySerializer(category).data, status=status.HTTP_200_OK)
        return Response({'message': 'Categoría no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        category_data = request.data
        updated_category = CategoryService.update_category(pk, category_data)
        if updated_category:
            return Response(CategorySerializer(updated_category).data, status=status.HTTP_200_OK)
        return Response({'message': 'Categoría no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        success = CategoryService.delete_category(pk)
        if success:
            return Response({'message': 'Categoría eliminada'}, status=status.HTTP_200_OK)
        return Response({'message': 'Categoría no encontrada'}, status=status.HTTP_404_NOT_FOUND)