from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from flask import Flask,request

# Create your views here.


def logout(request):
    return HttpResponse("logout")

@csrf_exempt
def login(request):
    result = False
    # print(request)
    if request.method=='POST':
       
        Email=request.POST.get('email')
        Pwd=request.POST.get('pwd')
        print(Email,Pwd)
        # result = True
        # return result

    return render (request,'login/login.html')
    