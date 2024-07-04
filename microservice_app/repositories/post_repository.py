

from microservice_app.models.category import Category
from microservice_app.models.post import Post
from microservice_app.models.user import User


class PostRepository:

    @staticmethod
    def add_post(post_data):
        post = Post(**post_data)
        post.save()
        return post
    
    @staticmethod
    def get_post_by_id(post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None
        
    @staticmethod
    def get_all_posts():
        return Post.objects.all()
    

    def update_post(post_id, post_data, files):
        try:
            post = Post.objects.get(id=post_id)
            user_id = post_data.get('user_id')

            # Ensure user_id is an integer
            if isinstance(user_id, User):
                user_id = user_id.id

            user = User.objects.get(id=user_id)
            post.title = post_data.get('title', post.title)
            post.content = post_data.get('content', post.content)
            post.category_id = post_data.get('category_id', post.category_id)
            post.user = user

            # Handle file update if any
            if 'image' in files:
                post.image = files['image']

            post.save()
            return post
        except Post.DoesNotExist:
            return None
    
    @staticmethod
    def delete_post(post_id):
        post = PostRepository.get_post_by_id(post_id)
        if post:
            post.delete()
            return True
        return False
    
    @staticmethod
    def get_posts_by_user_id(user_id):
        return Post.objects.filter(user_id=user_id)
    
    