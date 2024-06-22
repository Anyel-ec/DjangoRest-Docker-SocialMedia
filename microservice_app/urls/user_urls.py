from django.urls import include, path
from rest_framework import routers
from microservice_app.views.user_view import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    # path('users/<int:pk>/verify/', UserView.as_view({'post': 'verify_password'}), name='verify-password'),
    # path('users/verify/', UserView.as_view({'post': 'verify_password_with_email'}), name='verify-password-email'),
    # path('users/data/', UserView.as_view({'get': 'get_user_by_email'}), name='get-user-by-email'),
    # path('users/verify_exist/', UserView.as_view({'post': 'verify_exist_user'}), name='verify-exist-user'),
    # path('users/get_user/email/', UserView.as_view({'get': 'data'}), name='get-data'),
]