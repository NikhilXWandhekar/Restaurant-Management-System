from django.urls import path, include
from rest_framework import routers
from .views import RestaurantViewSet, MenuItemViewSet, TableViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'tables', TableViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]