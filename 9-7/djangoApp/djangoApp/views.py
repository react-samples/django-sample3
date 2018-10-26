from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    user = authenticate(
        username=request.POST.get('username'),
        password=request.POST.get('password')
    )
    login(request, user)
    return redirect('/')

def create_user_view(request):
    form = UserForm()
    return render(request, 'create_user_view.html', {'form': form})

def create_user(request):
    user = User.objects.create_user(
        request.POST.get('username'),
        request.POST.get('email'),
        request.POST.get('password')
    )
    user.save()
    return redirect('/accounts/login/')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
