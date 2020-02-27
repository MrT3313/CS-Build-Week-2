# IMPORTS
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    # room = RoomSerializer()
    class Meta:
        model = Room
        # fields = ('__all__')
        fields = [
            'room_id',
            'title',
            'description',
            'coordinates',
            'players',
            'items',
            'exits',
            'cooldown',
            'errors',
            'messages',
        ]