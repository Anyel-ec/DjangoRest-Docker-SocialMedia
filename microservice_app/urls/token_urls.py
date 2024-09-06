from django.urls import path, include
from rest_framework.routers import DefaultRouter
from microservice_app.views.TokenView import TokenView

router = DefaultRouter()
router.register(r'token', TokenView, basename='token')

urlpatterns = [
    path('', include(router.urls)),
]
