from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def log_in(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        if user_name:
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('index')

    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        con_pass = request.POST.get('con_password')

        if pass1 == con_pass:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'user already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already exist')
            else:
                user = User.objects.create(first_name=f_name, last_name=l_name, username=user_name, email=email,
                                           password=pass1)
                user.set_password(pass1)
                user.save()
                messages.success(request, 'registration done')
                return redirect('login')
        else:
            messages.error(request, 'password not matched')
    return render(request, 'registration.html')


def log_out(request):
    logout(request)
    return redirect('login')
