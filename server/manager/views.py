from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect
from student.models import *

# Create your views here.
def student_filter(request):
    return render(request, 'manager/student_filter.html', {'nav':'manager'})

@csrf_protect
def get_student_data(request):


    lan = Language.objects.get(name="English").cv.all()

    return HttpResponse('200')
