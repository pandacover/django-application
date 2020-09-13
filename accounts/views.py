from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Either username or Password does not match.')
            return redirect('login')
    else:
        return render(request, './login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username = None) or User.objects.filter(email = None) or User.objects.filter(first_name = None) or User.objects.filter(last_name = None):
            messages.info(request, 'Fill up all the details!')
            return redirect('register')

        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken!')
                return redirect('register')

            else:
                user = User.objects.creater_user(username=username, password=password1)
                user.save()
                return redirect('/')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, './register.html')