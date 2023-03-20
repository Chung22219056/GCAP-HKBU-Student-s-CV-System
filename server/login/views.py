from django.shortcuts import render
from django.shortcuts import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

# def login(request):
    # if request.method=='POST':
#         Email=request.POST.get('email')
#         Pwd=request.POST.get('password')
#         print(Email,Pwd)
#         # user=authenticate(request,Email=Email,Pwd=Pwd)
#         # if user is not None:
#         #     login(request,user)
#         #     return redirect('login.html')
#         # else:
#         #     return HttpResponse ("Username or Password is incorrect!!!")

    # return render(request, 'login/login.html')


def logout(request):
    return HttpResponse("logout")

# @csrf_exempt
def login(request):
    form = AuthenticationForm(request=request, data=request.POST)
    # print(form.data.items.)
    # print(Email)
    if request.method=='POST':
        # Email=request.POST.get['email']
        Pwd=request.POST.get('password')
        # print(Email,Pwd)
        # user=authenticate(request,Email=Email,Pwd=Pwd)
        # if user is not None:
        #     login(request,user)
        #     return redirect('login.html')
        # else:
        #     return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login/login.html')