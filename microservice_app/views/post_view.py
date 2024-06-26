from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.response import Response
from microservice_app.models.post import Post
from microservice_app.serializers.post_serializer import PostSerializer
from microservice_app.services.post_service import PostService

class PostView(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]  # Añadir parsers para multipart/form-data


    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            new_post = PostService.create_post(serializer.validated_data, request.FILES)
            return Response(PostSerializer(new_post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        posts = PostService.get_all_posts()
        return Response(PostSerializer(posts, many=True).data)
    
    def retrieve(self, request, pk=None):
        post = PostService.get_post(pk)
        if post:
            return Response(PostSerializer(post).data)
        return Response({'message': 'Post no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        post_data = request.data
        updated_post = PostService.update_post(pk, post_data)
        if updated_post:
            return Response(PostSerializer(updated_post).data)
        return Response({'message': 'Post no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        success = PostService.delete_post(pk)
        if success:
            return Response({'message': 'Post eliminado'}, status=status.HTTP_200_OK)
        return Response({'message': 'Post no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], url_path='by_user')
    def get_posts_by_user_id(self, request):
        user_id = request.query_params.get('user_id')
        posts = PostService.get_posts_by_user_id(user_id)
        return Response(PostSerializer(posts, many=True).data)
    
    @action(detail=False, methods=['get'], url_path='by_email')
    def get_posts_by_user_email(self, request):
        email = request.query_params.get('email')
        posts = PostService.get_posts_by_user_email(email)
        return Response(PostSerializer(posts, many=True).data)
