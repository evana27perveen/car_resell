from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from chat.models import Room, Message, SellerMessages
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    content = {

    }
    if request.method == 'GET':
        seller_name = request.GET.get('seller_name')
        room_name = request.GET.get('room_name')
        username = request.GET.get('username')
        if seller_name == username:
            seller_name = str(seller_name) + "(You)"
        content['seller'] = seller_name
        content['room_name'] = room_name
        content['username'] = username
    return render(request, 'chat/ChatHome.html', context=content)


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/ChatRoom.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    seller = request.POST['seller']
    if Room.objects.filter(name=room).exists():
        return redirect('/chat/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        user_buyer = User.objects.get(username=username)
        user_seller = User.objects.get(username=seller)
        to_seller = SellerMessages.objects.create(room_name=room, seller_name=user_seller, buyer_name=user_buyer)
        to_seller.save()
        new_room.save()
        return redirect('/chat/' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    this_room = Room.objects.get(name=room_id)
    new_message = Message.objects.create(value=message, user=username, room=this_room)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

