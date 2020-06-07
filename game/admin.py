from django.contrib import admin
from .models import *

class GuestUserAdmin(admin.ModelAdmin):
    fields = ('username', 'room_id')
    list_display = ('username', 'room_id')

class QuestionAdmin(admin.ModelAdmin):
    fields = ('img_path', 'answer')
    list_display = ('img_path', 'answer')

class RoomAdmin(admin.ModelAdmin):
    fields = ('room_id', 'host_user', 'roomname', 'no_of_players', 'no_of_rounds')
    list_display = ('room_id', 'host_user', 'roomname', 'no_of_players', 'no_of_rounds')

class MessageAdmin(admin.ModelAdmin):
    fields = ('author', 'content', 'timestamp')
    list_display = ('author', 'content', 'timestamp')

admin.site.register(GuestUser, GuestUserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Question, QuestionAdmin)
