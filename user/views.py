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
    username = request.session.get('username')
    if username:
        return HttpResponse(f'{username} 用户已登录')

    if request.method == 'GET':
        # username = request.COOKIES.get('username', '')
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
    try:
        user = Users.objects.get(username=username, password=password)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'login failed'})
    else:
        response = JsonResponse({'message': 'login success'})
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        if remember != 'true':
            request.session.set_expiry(0)
        # if remember == 'true':
        #     response.set_cookie('username', username, max_age=14*24*3600)
        return response
