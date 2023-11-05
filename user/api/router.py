from rest_framework.routers import DefaultRouter
from user.api.views import userViewSet, userModelViewSet

router_user = DefaultRouter()

router_user.register(prefix='user', basename='user', viewset=userModelViewSet)