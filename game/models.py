from django.db import models

# Create your models here.
class GuestUser(models.Model):
	username=models.CharField(max_length=30)
	roomname=models.CharField(max_length=50, null=True)

class Room(models.Model):
	host_user=models.CharField(max_length=30, null=True)
	roomname=models.CharField(max_length=50)
	no_of_players=models.CharField(max_length=50)
	no_of_rounds=models.CharField(max_length=50)