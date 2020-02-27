# from django.db import models
from django.contrib.gis.db import models

# Field Types
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.geos import Point


# Create your models here.
class Room(models.Model):
    room_id = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    coordinates = models.PointField(null=True)
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
        return self.room_id