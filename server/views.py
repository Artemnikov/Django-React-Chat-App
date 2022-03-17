import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Room, Message

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache, cache_control

from chat_app.auth_helper import get_sign_in_flow, get_token_from_code, remove_user_and_token, get_token, validate
from chat_app.graph_helper import get_user
from django.core.cache import cache

@csrf_exempt
def checkroom ( request ):
    room = json.loads(request.body).get('room')
    username = json.loads(request.body).get('username')
    data = json.dumps({
        'room': room,
        'username': username
    })
    
    if Room.objects.filter(name=room).exists():
        return HttpResponse('room found')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return HttpResponse('room created')

@csrf_exempt
def getMessages ( request ):
    room_req = json.loads(request.body).get('room')
    room_detail = Room.objects.get(name=room_req)
    messages = Message.objects.filter(room=room_detail.name)
    return JsonResponse({"messages" : list(messages.values())})

@csrf_exempt
def send ( request ):
    new_message = Message.objects.create(
        value = json.loads(request.body).get('message'),
        user = json.loads(request.body).get('username'),
        room = json.loads(request.body).get('room')
        )
    new_message.save()
    return HttpResponse('message saved')

def initialize_context ( request ):
    context = {}
    error = request.session.pop('flash_error', None)
    if error != None:
      context['errors'] = []
    context['errors'].append(error)
    # Check for user in the session
    context['user'] = request.session.get('user' , {'is_authenticated': False})
    return context

def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])

def sign_in ( request ):
#     # Get the sign-in flow
    flow = get_sign_in_flow()
#     # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
#     # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])

def sign_out ( request ):
    remove_user_and_token(request)
    return HttpResponseRedirect('')


@never_cache
def callback ( request ):
    # Make the token request
    result = get_token_from_code(request)
    # print(result)
    username = result['id_token_claims']['name']
    response = HttpResponseRedirect('/lobby')
    response.set_cookie('username', username)
    validate(result.get('id_token'))
    
    return response
