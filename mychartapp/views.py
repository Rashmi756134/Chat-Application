from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='login')
def Homepage(request):
    return render (request,'home.html')

def signuppage(request):
    if request.method == 'POST':
        uname=request.POST.get('Username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already exists!")
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request,'signup.html')

def Loginpage(request):
    if request.method == 'POST':
        uname=request.POST.get('Username')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('create-room')
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def portfolio(request):
    return render (request,'portfolio.html')

def logoutpage(request):
    logout(request)
    return render (request,'login.html')

# def chatroom(request):
#     return render (request,'chatroom.html')

def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        
        try :
            get_room = Room.objects.get(room_name=room) 
            return redirect('room', room_name=room, username=username)
         
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('room', room_name=room, username=username)
                     
    return render(request,'chatroom.html')

def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name = room_name)
    
    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages = Message.objects.filter(room=get_room)
    
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    } 
    return render(request,'message.html',context)

def contact(request):
    return render (request,'contact.html')

def message(request):
    return render(request,'message.html')
    