from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)


class SellerMessages(models.Model):
    room_name = models.CharField(max_length=1000000)
    seller_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='seller')
    buyer_name = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='buyer')
