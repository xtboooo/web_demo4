from django.shortcuts import render, HttpResponse, redirect
from user.models import Users


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f'username:{username}  password:{password}')
        user = Users.objects.create(username=username, password=password)
        return redirect('/login/')


def login(request):
    return render(request, 'login.html')
