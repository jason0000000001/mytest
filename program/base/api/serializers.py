from rest_framework.serializers import ModelSerializer
from base.models import Data6
from base.models import User6
from base.models import Medicine
from base.models import test


class UserSerializer(ModelSerializer):
    class Meta:
        model = User6
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = '__all__'


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class Room1Serializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['weight','temperature','pressures','pressured','heartbeat','bmi','bmr']


class TestSerializer(ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'



class RoomweightSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['weight']


class RoomtemperatureSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['temperature']


class RoompressuresSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['pressures']


class RoompressuredSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['pressured']


class RoomheartbeatSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['heartbeat']





'''
class RoombSerializer(ModelSerializer):
    class Meta:
        model = Data7
        fields = ['bmi']
'''
