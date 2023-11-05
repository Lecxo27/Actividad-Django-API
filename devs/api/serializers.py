from rest_framework.serializers import ModelSerializer
from devs.models import Dev
class DevSerializer(ModelSerializer):
    class Meta:
        model = Dev
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'years', 'country']