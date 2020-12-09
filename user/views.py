from django.shortcuts import render, HttpResponse, redirect
from user.models import Users
from django.http import JsonResponse

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
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
    try:
        user = Users.objects.get(username=username, password=password)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'login failed'})
    else:
        return JsonResponse({'message': 'login success'})
