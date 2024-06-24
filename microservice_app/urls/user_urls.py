from django.urls import include, path
from rest_framework import routers
from microservice_app.views.user_view import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
   
]