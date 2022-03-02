from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def main (request):
    room =  json.loads(request.body).get('room')
    username = json.loads(request.body).get('username')
    room_details = Room.objects.get(name=room)
    
    return HttpResponse({
        'username': username,
        'room': room,
        'room_details': room_details
    })
    
@csrf_exempt
def checkroom(request):
    room = json.loads(request.body).get('room')
    username = json.loads(request.body).get('username')
    data = json.dumps({
        'room': room,
        'username': username
    })
    if Room.objects.filter(name=room).exists():
        return HttpResponse(data)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return HttpResponse(data)

@csrf_exempt
def getMessages(request):
    room_req = json.loads(request.body).get('room')
    room_detail = Room.objects.get(name=room_req)
    messages = Message.objects.filter(room=room_detail.name)
    return JsonResponse({"messages" : list(messages.values())})

@csrf_exempt
def send(request):
    message = json.loads(request.body).get('message')
    user = json.loads(request.body).get('username')
    room = json.loads(request.body).get('room')

    new_message = Message.objects.create(value=message, user=user, room=room)
    new_message.save()
    print(new_message.values())
    return HttpResponse(new_message)