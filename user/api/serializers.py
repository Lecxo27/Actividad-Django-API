from rest_framework.serializers import ModelSerializer
from user.models import users

class UserSerializer(ModelSerializer):
    class Meta:
        model = users
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email',]