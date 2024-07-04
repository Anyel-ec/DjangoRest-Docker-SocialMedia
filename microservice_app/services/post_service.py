
from microservice_app.models.post import Post
from microservice_app.repositories.post_repository import PostRepository


class PostService:

    @staticmethod
    def create_post(post_data, files):
        post = Post(**post_data)
        if 'image' in files:
            post.image = files['image']
        post.save()
        return post
    

    @staticmethod
    def get_post(post_id):
        return PostRepository.get_post_by_id(post_id)
    
    @staticmethod
    def get_all_posts():
        return PostRepository.get_all_posts()
    

    def update_post(post_id, post_data, files):
        # Ensure post_data contains 'user_id' as an integer
        if 'user_id' in post_data and isinstance(post_data['user_id'], str):
            post_data['user_id'] = int(post_data['user_id'])
        return PostRepository.update_post(post_id, post_data, files)

    
    @staticmethod
    def delete_post(post_id):
        return PostRepository.delete_post(post_id)
    
    @staticmethod
    def get_posts_by_user_id(user_id):
        return PostRepository.get_posts_by_user_id(user_id)
    
    