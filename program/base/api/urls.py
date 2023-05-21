from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('getmedicine/<str:pk>/', views.get),
    #path('users/', views.getUsers),
    #path('users/<str:pk>/', views.getUser),
    path('users/', views.createUser),
    path('users/<str:pk>/', views.updateUser),
    #path('updateusers/<str:pk>/', views.updateUser),
    #path('deleteusers/<str:pk>/', views.deleteUser),
    #path('datas/', views.getRooms),
    # #path('datas/<str:pk>/', views.getRoom),
    path('datas/', views.createRoom),
    path('datas/<str:pk>/', views.updateRoom),
    path('<str:pk>/medicine/', views.getmedicine),
    path('medicine/', views.createmedicine),
    path('medicine/<str:pk>/', views.updatemedicine),
    #path('datasname/<str:pk>/', views.getRoomname),
    path('datasid/<str:pk>/', views.getRoomid),
    path('history/<str:pk>/', views.gethistory),
    path('datastime/<str:pk>/<str:sk>/<str:ek>/', views.getRoomtime),#YYYY-MM-DDTHH:MM:SS
    path('test/', views.gettest),
    path('<str:pk>/weight/', views.getweight),
    path('<str:pk>/temperature/', views.gettemperature),
    path('<str:pk>/pressures/', views.getpressures),
    path('<str:pk>/pressured/', views.getpressured),
    path('<str:pk>/heartbeat/', views.getheartbeat),
    path('table/<str:pk>/', views.gettable),
    #path('h/<str:pk>/', views.geth),
    #path('deleteusers/<str:pk>/data', views.deleteRoom),
    #path('test/', views.testRoom),
]