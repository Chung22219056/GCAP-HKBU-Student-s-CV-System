from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect

# Create your views here.
def student_filter(request):
    return render(request, 'manager/student_filter.html', {'nav':'manager'})

@csrf_protect
def get_student_data(request):
    if request.method == 'GET':
        return JsonResponse({'foo':[1,2,3]})
    return HttpResponse('404')