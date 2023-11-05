from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from devs.models import Dev
from devs.api.serializers import DevSerializer



class DevApiView(APIView):
    def get(self, request):
        # devs = Dev.objects.all()
        # devs = [dev.first_name for dev in Dev.object.all()]

        devs = DevSerializer(Dev.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=devs.data)

    def post(self,request):
       # Dev.objects.create(
        #    first_name = request.POST['first_name'],
        #    last_name=request.POST['last_name'],
        #    email=request.POST['email'],
        #    years=request.POST['years'],
        #    country=request.POST['country'],
        #)
       # return self.get(request)

        devs = DevSerializer(data = request.POST)
        devs.is_valid(raise_exception=True)
        devs.save()
        return Response(status=status.HTTP_200_OK, data=devs.data)

class DevViewSet(ViewSet):
    def list(self, request):

        devs = DevSerializer(Dev.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=devs.data)

    def create(self, request):
        devs = DevSerializer(data = request.POST)
        devs.is_valid(raise_exception=True)
        devs.save()
        return Response(status=status.HTTP_200_OK, data=devs.data)

class DevModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DevSerializer
    queryset = Dev.objects.all()