from django.urls import include, path
from rest_framework import routers
from microservice_app.views.GenderViewSet import GenderViewSet

router = routers.DefaultRouter()
router.register(r'genders', GenderViewSet, basename='genders')

urlpatterns = [
    path('', include(router.urls)),
]
