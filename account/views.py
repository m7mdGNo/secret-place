from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .models import Message,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *



def Logout(request):
    logout(request)
    return redirect('home')

def home(request):
    user = request.user
    no_of_members = User.objects.all()
    form = no_of_members.count()
    if user.is_authenticated:
        profile = request.user.Profile
        messages_box = user.Profile.message_set.all().order_by('-created_at')
        num_of_messages = messages_box.count()

        return render(request, 'profile.html', {'messages_box': messages_box,'num':num_of_messages,'profile':profile})
    return render(request, 'home.html',{'form':form})


def Register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if User.objects.filter(username=username).first():
            messages.success(request, 'Username is taken.')
            return redirect('register')

        user_obj = User(username=username ,first_name=first_name,last_name=last_name ,email=email)
        user_obj.set_password(password1)
        if password1 == password2:
            user_obj.save()
        profile_obj = Profile.objects.create(user=user_obj,username=username,first_name=first_name,last_name=last_name,email=email)
        profile_obj.save()
        return redirect('login')
    return render(request,'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()
        Profile.objects.filter(user=user_obj).first()
        user = authenticate(username=username, password=password)
        if user_obj is None:
            messages.success(request, 'User not found.')
        else:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def Profile_User(request, pk):
    profile = User.objects.get(id=pk).Profile
    if request.user.is_authenticated:
        if profile == request.user.Profile:
            return redirect('home')
    text = request.POST.get('text')
    if text == None:
        pass
    else:
        Message.objects.create(text=text,user=profile)
        messages.success(request,'send successfully')
    return render(request, 'send.html', {"profile":profile})

@login_required(login_url='login')
def setting(request):
    form = ProfileForm(instance=request.user.Profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.Profile)

        if form.is_valid():
            form.save()
            messages.success(request,'updated successfully')
    return render(request,'settings.html',{'form':form})



def search(request):
    form = Profile.objects.all()
    return render(request,'search.html',{'form':form})
