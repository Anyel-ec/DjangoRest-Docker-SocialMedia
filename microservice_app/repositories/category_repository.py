from microservice_app.models.category import Category


class CategoryRepository:
   
    def __init__(self):
        self.model = Category
        # Agregar 3 categorías predefinidas si no existen
        if not self.model.objects.exists():
            self.add_category(name='Tecnología', description='Todo sobre lo último en tecnología.')
            self.add_category(name='Salud', description='Consejos y noticias sobre salud y bienestar.')
            self.add_category(name='Estilo de vida', description='Artículos sobre estilo de vida y vivir.')

    @staticmethod
    def add_category(category_data):
        category = Category(**category_data)
        category.save()
        return category
    
    @staticmethod
    def get_category_by_id(category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return None
        
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    

    @staticmethod
    def update_category(category_id, category_data):
        category = CategoryRepository.get_category_by_id(category_id)
        if category:
            for key, value in category_data.items():
                setattr(category, key, value)
            category.save()
            return category
        return None
    
    @staticmethod
    def delete_category(category_id):
        category = CategoryRepository.get_category_by_id(category_id)
        if category:
            category.delete()
            return True
        return False
    
    