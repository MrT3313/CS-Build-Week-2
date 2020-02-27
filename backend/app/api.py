# IMPORTS
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework.views import APIView

# ?? 
from django.forms.models import model_to_dict

# MODELS
# from . import models
from .models import *

class Test(APIView):
    def get(self, request):
        # Response
        response = {"Status": 200}
        return JsonResponse(response)

class GetRooms(APIView):
    def get(self, request):
        rooms = Room.objects.all()

        response = []
        for item in rooms:
            item = model_to_dict(item)
            response.append(item)

        return JsonResponse(response, safe=False)

class Traverse(APIView):
    def get(self, request):
        pass
        