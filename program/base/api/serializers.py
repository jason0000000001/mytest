from rest_framework.serializers import ModelSerializer
from base.models import Data


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'