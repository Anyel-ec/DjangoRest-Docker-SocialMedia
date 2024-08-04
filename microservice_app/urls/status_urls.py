from django.urls import include, path
from rest_framework import routers
from microservice_app.views.StatusViewSet import StatusViewSet

router = routers.DefaultRouter()
router.register(r'statuses', StatusViewSet, basename='statuses')

urlpatterns = [
    path('', include(router.urls)),
]
