# services/user_service.py

from hashlib import sha256
import uuid
from django.core.exceptions import ValidationError
from microservice_app.repositories.user_repository import UserRepository

class UserService:

    @staticmethod
    def create_user(user_data):
        password = user_data['password']
        salt = uuid.uuid4().hex
        hashed_password = sha256((salt + password).encode()).hexdigest()

        user_data['password'] = hashed_password
        user_data['salt'] = salt

        try:
            new_user = UserRepository.add_user(user_data)
            return new_user
        except ValidationError as e:
            return {'error': str(e)}

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def update_user(user_id, user_data):
        if 'password' in user_data:
            password = user_data['password']
            salt = uuid.uuid4().hex
            hashed_password = sha256((salt + password).encode()).hexdigest()
            user_data['password'] = hashed_password
            user_data['salt'] = salt

        updated_user = UserRepository.update_user(user_id, user_data)
        return updated_user

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)

    @staticmethod
    def verify_password(user_id, password):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            hashed_password = sha256((user.salt + password).encode()).hexdigest()
            if hashed_password == user.password:
                return True
        return False

    @staticmethod
    def verify_password_with_email(email, password):
        user = UserRepository.get_user_by_email(email)
        if user:
            hashed_password = sha256((user.salt + password).encode()).hexdigest()
            if hashed_password == user.password:
                return True
        return False

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.get_user_by_email(email)

    @staticmethod
    def verify_exist_user(email):
        return UserRepository.verify_exist_user(email)
