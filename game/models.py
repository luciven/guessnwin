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

class Message(models.Model):
	author = models.ForeignKey(GuestUser, related_name="author_messages", on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author.username

	def last_50_messages(roomId):
		return Message.objects.order_by('timestamp').filter('room'.roomname==roomId)[:50]