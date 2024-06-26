from django.urls import include, path
from rest_framework import routers
from microservice_app.views.post_view import PostView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'posts', PostView, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)