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
                room_id=request.POST.get('roomname')
                next = room_id+'/'
                return HttpResponseRedirect(next) 

class RoomView(TemplateView):
    template_name= 'room.html'

    def room(self, request, room_name):
        return render(request, self.template_name, {
            'room_name': room_name
        })

class CreateRoomView(TemplateView):
    template_name= 'createroom.html'

    def get(self, request):
        form = RoomForm()
        return render(request, self.template_name, {
            'form':form,
            })

    def post(self, request):
        if request.method == 'POST':
            form=RoomForm(request.POST)
            if form.is_valid():
                form.save()
                room_id=request.POST.get('roomname')
                next = '/game/'+room_id+'/'
                return HttpResponseRedirect(next)
            else:
                print(type(request.POST.get('no_of_players')))
                print(request.POST.get('no_of_players'))
                return render(request, self.template_name, {
                    'form':form,
                    })


    # def form_valid(self, form):
    #     self.object = form.save(commit=False)

    #     self.object.save()
