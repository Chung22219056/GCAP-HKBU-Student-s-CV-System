from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect
<<<<<<< HEAD
# from .models import dbData


=======
from student.models import *
>>>>>>> eb45f165e5ebd02f597812aa255f17194754887d

# Create your views here.
def student_filter(request):
    return render(request, 'manager/student_filter.html', {'nav':'manager'})

@csrf_protect
def get_student_data(request):
<<<<<<< HEAD
    if request.method == 'GET':
        return JsonResponse({'foo':[1,2,3]})
    return HttpResponse('404')

# @csrf_protect
# def get_student_data(request):
#     data = dbData.objects.all()
#     return JsonResponse(data)
#     # return HttpResponse('404')
=======


    lan = Language.objects.get(name="English").cv.all()

    return HttpResponse('200')
>>>>>>> eb45f165e5ebd02f597812aa255f17194754887d
