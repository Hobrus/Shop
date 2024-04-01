from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoodsViewSet

router = DefaultRouter()
router.register(r'goods', GoodsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]