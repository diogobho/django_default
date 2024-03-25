from django.shortcuts import render,redirect
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')
    