from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from student.models import *


# Create your views here.


def logout(request):
    return HttpResponse("logout")

@csrf_exempt
def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user and user.check_password(password):
                auth_login(request, user)
                try:
                    student = Student.objects.get(user_id=user)
                    return JsonResponse({"status":True, "is_student": True})
                except:
                    return JsonResponse({"status":True, "is_student": False})
            else:
                #return render(request,'login/login.html',{"login_failed":True})
                return JsonResponse({"status":False})
        except User.DoesNotExist:
            #return render(request,'login/login.html',{"login_failed":True})
            return JsonResponse({"status":False})

    return render (request,'login/login.html')
    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')