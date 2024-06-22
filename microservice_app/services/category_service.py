
from microservice_app.repositories.category_repository import CategoryRepository

class CategoryService:

    @staticmethod
    def create_category(category_data):
        new_category = CategoryRepository.add_category(category_data)
        return new_category
    
    @staticmethod
    def get_category(category_id):
        return CategoryRepository.get_category_by_id(category_id)
    
    @staticmethod
    def get_all_categories():
        return CategoryRepository.get_all_categories()
    
    @staticmethod
    def update_category(category_id, category_data):
        updated_category = CategoryRepository.update_category(category_id, category_data)
        return updated_category
    
    @staticmethod
    def delete_category(category_id):
        return CategoryRepository.delete_category(category_id)