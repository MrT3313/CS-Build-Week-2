# from django.db import models
from django.contrib.gis.db import models

# Field Types
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.geos import Point

# TODO: Should I add a direction room => {'n_room': 37} / {'s_room': 35}

# Create your models here.
class Room(models.Model):
    room_id = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    coordinates = models.CharField(max_length=50, null=True)
    # coordinates = models.PointField(null=True)
    elevation = models.IntegerField(null=True)
    terrain = models.CharField(max_length=50)
    players = ArrayField(
        models.CharField(max_length=50),
        null=True
    )
    items = ArrayField(
        models.CharField(max_length=50),
        null=True
    )
    exits = ArrayField(
        models.CharField(max_length=1),
        size=4,
        null=True
    )
    cooldown = models.IntegerField(null=True)
    errors = ArrayField(
        models.TextField(max_length=100, blank=True),
        null=True
    )
    messages = ArrayField(
        models.CharField(max_length=100, blank=True),
        null=True
    )

    def __str__(self):
        return f'{self.room_id}'

class Graph_Exploration(models.Model):
    room_id = models.IntegerField()
    n = models.CharField(max_length=5)
    s = models.CharField(max_length=5)
    e = models.CharField(max_length=5)
    w = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.room_id}'
    