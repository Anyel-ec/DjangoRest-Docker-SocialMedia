from django.urls import include, path
from rest_framework import routers
from microservice_app.views.category_view import CategoryView

router = routers.DefaultRouter()
router.register(r'categories', CategoryView, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]