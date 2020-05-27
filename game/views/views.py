from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from game.forms import *
from game.models import *
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = GuestUserForm()
        return render(request, self.template_name, {
            'form':form,
            })

    def post(self, request):
        if request.method == 'POST':
            form=GuestUserForm(request.POST)
            if form.is_valid():
                form.save()
                room_id=request.POST.get('room_id')
                username=request.POST.get('username')
                request.session['member_id'] = username
                #print("in home view",request.session['member_id'])
                next = room_id+'/'
                return HttpResponseRedirect(next) 

class RoomView(TemplateView):
    template_name= 'layout.html'

    def get(self, request, room_id):
        #print("in roomview1")
        #print("in roomview",request.session['member_id'])
        return render(request, self.template_name, {
            'room_id': room_id,
            'username': request.session['member_id']
        })

class CreateRoomView(TemplateView):
    template_name= 'createroom.html'

    def get(self, request):
        while True:
            roomId = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 6))
            if Room.objects.filter(room_id=roomId).exists():
                continue
            break
        print("Res:", roomId)
        form = RoomForm()
        return render(request, self.template_name, {
            'form':form,
            'room_id':roomId,
            })

    def post(self, request):
        if request.method == 'POST':
            form=RoomForm(request.POST)
            if form.is_valid():
                form.save()
                room_id=request.POST.get('room_id')
                print('room:', room_id)
                username=request.POST.get('host_user')
                request.session['member_id'] = username
                GuestUser.objects.create(
                    username=username,
                    room_id=room_id
                    )
                next = '/game/'+room_id+'/'
                print("next:",room_id)
                return HttpResponseRedirect(next)
            else:
                #print(type(request.POST.get('no_of_players')))
                #print(request.POST.get('no_of_players'))
                return render(request, self.template_name, {
                    'form':form,
                    })

