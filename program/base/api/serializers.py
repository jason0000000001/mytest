from rest_framework.serializers import ModelSerializer
from base.models import Data6
from base.models import User6
from base.models import test

class UserSerializer(ModelSerializer):
    class Meta:
        model = User6
        fields = '__all__'
        #fields = ['image_id','name','birthday','sex','height','weight','temperature','pressures','pressured']


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = '__all__'


class AllSerializer(ModelSerializer):
    class Meta:
        model = User6,Data6
        #fields = '__all__'
        fields = ['image_id','name','birthday','sex','height','weight','temperature','pressures','pressured']


class RoomwSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['weight']

class UserhSerializer(ModelSerializer):
    class Meta:
        model = User6
        fields = ['name','height']

class RoombSerializer(ModelSerializer):
    class Meta:
        model = Data6
        fields = ['bmi']

