from django.shortcuts import render, HttpResponse
from user.models import Users


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(f'username:{username}  password:{password}')
        user = Users.objects.create(username=username, password=password)
        return HttpResponse('注册成功')
