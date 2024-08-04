from django.urls import include, path
from rest_framework import routers
from microservice_app.views.ProvinceViewSet import ProvinceViewSet

router = routers.DefaultRouter()
router.register(r'provinces', ProvinceViewSet, basename='provinces')

urlpatterns = [
    path('', include(router.urls)),
]
