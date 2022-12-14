from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Data6
from base.models import User6
from .serializers import RoomSerializer
from .serializers import UserSerializer
#from .serializers import UserhSerializer
#from .serializers import AllSerializer
#from .serializers import RoomwSerializer
#from .serializers import RoombSerializer
from django.http import HttpResponse, JsonResponse


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        #'GET /api/users',
        'GET,POST /api/users/',
        'GET.POST,DELETE /api/users/:id',
        #'POST /api/updateusers/:id',
        #'DELETE /api/deleteusers/:id',
        #'GET /api/datas',
        'GET /api/users/:id/data',
        'GET /api/userss/:name/data',
        'GET,POST /api/datas',
        'GET,POST,DELETE /api/datas/:id/',
        #'DELETE /api/deleteusers/:id/data',
    ]
    return Response(routes)

'''
@api_view(['GET'])
def getUsers(request):
    users = User6.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = User6.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getall(request, pk):
    all = User6.objects.filter(name=pk)
    serializer = AllSerializer(all, many=True)
    all = Data6.objects.filter(names=pk)
    serializer = AllSerializer(all, many=True)
    return Response(serializer.data)
'''

@api_view(['POST', 'GET'])
def createUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User succsesfully create!')
    else:
        users = User6.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    '''
    return Response({
        "image_id": 1,
        "name": "tom",
        "birthday": "2000/01/01",
        "sex": "m",
        "height": 180.0
    })
    '''
	#serializer = RoomSerializer(room=request.data)

	#if serializer.is_valid():
		#serializer.save()

	#return Response(serializer.data)
    '''
        "image_id": 1,
        "name": "tom",
        "birthday": "2000/01/01",
        "sex": "m",
        "temperature": 36.0,
        "weight": 55.0,
        "height": 180.0,
        "pressures": 55,
        "pressured": 55
    '''
@api_view(['POST', 'GET', 'DELETE'])
def updateUser(request, pk):
	#room = Data.objects.get(id=pk)
    if request.method == 'POST':
        user = User6.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        #serializer = RoomSerializer(room, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response('User succsesfully update!')
    elif request.method == 'DELETE':
        user = User6.objects.get(id=pk)
        user.delete()
        return Response('User succsesfully delete!')
    else:
        user = User6.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

	#serializer = RoomSerializer(instance=room, room=request.data)

	#if serializer.is_valid():
		#serializer.save()

	#return Response(serializer.data)

'''
@api_view(['DELETE', 'GET'])
def deleteUser(request, pk):
	#room = Data.objects.get(id=pk)
	#room.delete()
    if request.method == 'DELETE':
        user = User6.objects.get(id=pk)
        user.delete()
        return Response('User succsesfully delete!')
    user = User6.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

	#return Response('Item succsesfully delete!')
'''
'''
@api_view(['GET'])
def getRooms(request):
    rooms = Data6.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)
'''

@api_view(['GET'])
def getRoom(request, pk):
    room = Data6.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def getRoomname(request, pk):
    rooms = Data6.objects.filter(userid=pk)
    serializer = RoomSerializer(rooms, many=True)
    #for keys, values in serializer.item():
    return Response(serializer.data)
'''
    user = User6.objects.get(id=pk)
    serializer = UserhSerializer(user, many=False)
    height = serializer.data["height"]
    print(height)
    serializer = RoomwSerializer(rooms, many=True)
    weight = serializer.data[0]["weight"]
    print(weight)
    bmi = weight / (height/100.0) ** 2.0
    print(bmi)
    #serializer = RoomSerializer(data=request.data)
'''
    
'''
room = Data6.objects.get(userid=pk)
        user = User6.objects.get(id=pk)
        serializer = UserhSerializer(user, many=False)
        height = serializer.data["height"]
            #print(height)
        serializer = RoomwSerializer(rooms, many=True)
        weight = serializer.data[0]["weight"]
            #print(weight)
        bmi = weight / (height/100.0) ** 2.0
            #print(bmi)    

@api_view(['POST', 'GET'])
def createRoom(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Item succsesfully create!')
    else:
        rooms = Data6.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
'''
'''
    return Response({
        #"name": "test",
        #"userid": 1,
        "weight": 55.0,
        "temperature": 36.0,
        "pressures": 55,
        "pressured": 55
    })
'''

@api_view(['POST', 'GET', 'DELETE'])
def updateRoom(request, pk):
	#room = Data.objects.get(id=pk)
    if request.method == 'POST':
        room = Data6.objects.get(id=pk)
        serializer = RoomSerializer(instance=room, data=request.data)
        #serializer = RoomSerializer(room, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response('Item succsesfully update!')
    elif request.method == 'DELETE':
        room = Data6.objects.get(id=pk)
        room.delete()
        return Response('Item succsesfully delete!')
    else:
        room = Data6.objects.get(id=pk)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)

'''
@api_view(['DELETE', 'GET'])
def deleteRoom(request, pk):
	#room = Data.objects.get(id=pk)
	#room.delete()
    if request.method == 'DELETE':
        room = Data6.objects.get(id=pk)
        room.delete()
        return Response('Item succsesfully delete!')
    room = Data6.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
'''


@api_view(['POST', 'GET'])
def createRoom(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            userid = serializer.validated_data['userid']
            weight = serializer.validated_data['weight']
            temperature = serializer.validated_data['temperature']
            pressures = serializer.validated_data['pressures']
            pressured = serializer.validated_data['pressured']
            bmi = serializer.validated_data['bmi']
            bmr = serializer.validated_data['bmr']
            result1 = serializer.validated_data['result1']
            result2 = serializer.validated_data['result2']
            result3 = serializer.validated_data['result3']
            user = User6.objects.get(name=userid)
            serializer1 = UserSerializer(user, many=False)
            height = serializer1.data['height']
            sex = serializer1.data['sex']
            birthday = serializer1.data['birthday']
            birthday1 = birthday.split('/')
            year = int(birthday1[0])
            month = int(birthday1[1])
            day = int(birthday1[2])
            age = 2023 - year
            #--BMI??????
            bmi = weight / (height/100.0) ** 2.0
            bmi = round(bmi, 1)
            serializer.validated_data['bmi'] = bmi
            print(bmi)
            #--BMR??????
            if sex == "male":
                bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            else:
                bmr = 655 + 9.6 * weight +1.8 * height - 4.7 * age
                bmr = round(bmr, 1)
                serializer.validated_data['bmr'] = bmr
            print(bmr)
            ##--????????????
            if pressures>140.0:
                if pressured>90.0:
                    result1 = ('????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('???????????????????????????,?????????????????????,??????20???30??????,????????????????????????')
                    serializer.validated_data['result1'] = result1
            elif pressures>100.0:
                if pressured>90.0:
                    result1 = ('???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('?????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
            else:
                if pressured>90.0:
                    result1 = ('?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                elif pressured>70.0:
                    result1 = ('?????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
                else:
                    result1 = ('?????????????????????????????????????????????????????????????????????????????????????????????????????????')
                    serializer.validated_data['result1'] = result1
            ##--????????????
            if temperature >38.0:
                result2 = ('??????????????????????????????????????????????????????')
                serializer.validated_data['result2'] = result2
            elif temperature >37.0:
                result2 = ('?????????????????????????????????????????????')
                serializer.validated_data['result2'] = result2
            else:
                result2 = ("????????????????????????????????????????????????????????????Covid Nineteen???")
                serializer.validated_data['result2'] = result2
            ##--BMI??????
            if bmi >= 27.0:
                result3 = ('??????')
                serializer.validated_data['result3'] = result3
            elif 27.0 > temperature >= 24.0:
                result3 = ('????????????')
                serializer.validated_data['result3'] = result3
            elif 24.0 > temperature >= 18.5:
                result3 = ('????????????')
                serializer.validated_data['result3'] = result3
            else:
                result3 = ("????????????")
                serializer.validated_data['result3'] = result3
            print(result1)
            print(result2)
            print(result3)
            serializer.save()
            
            return Response('Item succsesfully create!')
    else:
        rooms = Data6.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)