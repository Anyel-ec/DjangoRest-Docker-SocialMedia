from django.urls import path
from microservice_app.controller.user_controller import UserController

urlpatterns = [
    path('users/', UserController.as_view(), name='user-list'),
    path('users/<int:user_id>/', UserController.as_view(), name='user-detail'),
    path('users/<int:user_id>/verify/', UserController.verify_password, name='verify-password'),
    path('users/verify/', UserController.verify_password_with_email, name='verify-password-email'),
    path('user/data/', UserController.get_user_by_email, name='get-user-by-email'),
    path('users/verify_exist/', UserController.verify_exist_user, name='verify-exist-user'),
]