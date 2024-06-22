
from microservice_app.repositories.post_repository import PostRepository


class PostService:

    @staticmethod
    def create_post(post_data):
        new_post = PostRepository.add_post(post_data)
        return new_post
    

    @staticmethod
    def get_post(post_id):
        return PostRepository.get_post_by_id(post_id)
    
    @staticmethod
    def get_all_posts():
        return PostRepository.get_all_posts()
    
    @staticmethod
    def update_post(post_id, post_data):
        updated_post = PostRepository.update_post(post_id, post_data)
        return updated_post
    
    @staticmethod
    def delete_post(post_id):
        return PostRepository.delete_post(post_id)
    
    @staticmethod
    def get_posts_by_user_id(user_id):
        return PostRepository.get_posts_by_user_id(user_id)
    
    