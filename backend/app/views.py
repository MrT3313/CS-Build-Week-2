# Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Models
from .models import Room
from .serializers import RoomSerializer

# Scripts
from .scripts.traverse import traverse_server

# Pre Installed
from django.shortcuts import render

# Create your views here.
@api_view(['GET', ] )
def Rooms_View(request):
    try: 
        rooms = Room.objects.all()
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

@api_view(['GET', ])
def Test_Script(request):
    result = traverse_server()
    return Response(result)
    