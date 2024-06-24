

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
    
    @staticmethod
    def update_post(post_id, post_data):
        post = PostRepository.get_post_by_id(post_id)
        if post:
            if 'user_id' in post_data:
                post_data['user_id'] = User.objects.get(id=post_data['user_id'])
            if 'category_id' in post_data:
                post_data['category_id'] = Category.objects.get(id=post_data['category_id'])
            for key, value in post_data.items():
                setattr(post, key, value)
            post.save()
            return post
        return None
    
    def delete_post(post_id):
        post = PostRepository.get_post_by_id(post_id)
        if post:
            post.delete()
            return True
        return False
    
    @staticmethod
    def get_posts_by_user_id(user_id):
        return Post.objects.filter(user_id=user_id)
    
    