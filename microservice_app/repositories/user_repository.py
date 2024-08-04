from microservice_app.models.user import User
from django.core.exceptions import ValidationError

class UserRepository:

    @staticmethod
    def add_user(user_data):
        if UserRepository.verify_exist_user(user_data['email'], user_data.get('username')):
            raise ValidationError("User with this email or username already exists")
        
        user = User(**user_data)
        user.save()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def update_user(user_id, user_data):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            user.save()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            user.delete()
            return True
        return False

    @staticmethod
    def verify_exist_user(email, username=None):
        if username:
            return User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()
        return User.objects.filter(email=email).exists()
