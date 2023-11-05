from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from user.models import users
from user.api.serializers import UserSerializer

class UserApiView(APIView):
    def get(self, request):

        liuser = UserSerializer(users.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=liuser.data)

    def post(self,request):

        liuser = UserSerializer(data = request.POST)
        liuser.is_valid(raise_exception=True)
        liuser.save()
        return Response(status=status.HTTP_200_OK, data=liuser.data)

class userViewSet(ViewSet):
    def list(self, request):
            devs = UserSerializer(users.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data=devs.data)

    def create(self, request):
            liuser = UserSerializer(data=request.POST)
            liuser.is_valid(raise_exception=True)
            liuser.save()
            return Response(status=status.HTTP_200_OK, data=liuser.data)

class userModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = users.objects.all()