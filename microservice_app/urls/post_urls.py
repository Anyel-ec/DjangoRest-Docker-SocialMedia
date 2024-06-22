from django.urls import include, path
from rest_framework import routers
from microservice_app.views.post_view import PostView

router = routers.DefaultRouter()
router.register(r'posts', PostView, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]