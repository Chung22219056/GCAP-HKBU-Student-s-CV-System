from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'manager/dashboard.html')


def accounts(request):
    return render(request, 'manager/accounts.html')
