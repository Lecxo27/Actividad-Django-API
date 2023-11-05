from rest_framework.routers import DefaultRouter
from devs.api.views import DevViewSet, DevModelViewSet

router_dev = DefaultRouter()

# router_dev.register(prefix='devs', basename='devs', viewset='DevViewSet')
router_dev.register(prefix='devs', basename='devs', viewset=DevModelViewSet)