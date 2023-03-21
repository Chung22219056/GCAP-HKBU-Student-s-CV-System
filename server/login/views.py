from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.


def logout(request):
    return HttpResponse("logout")

@csrf_exempt
def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        if user and user.check_password(password):
            auth_login(request, user)
            return HttpResponse("200 ok")
        else:
            return render(request,'login/login.html',{"login_failed":True})

    return render (request,'login/login.html')
    