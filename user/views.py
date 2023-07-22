from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['pass1']
        pass2 = request.POST['pass2']
        if password == pass2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'user name alerady taken.')
                return redirect('/user/register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    password=password)
                user.save()
                messages.info(request, 'user created')
                return redirect('/user/login')
        else:
            messages.info(request, 'password not match')
            return redirect('/user/register')

    return render(request, 'user/register.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('/user/login')
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
