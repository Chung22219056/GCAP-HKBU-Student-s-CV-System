from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect
from student.models import *
import json

# Create your views here.
def student_filter(request):
    students = [{'student_id':student.student_id, 'student_name': student.getName(), 'language':[lan.name for lan in Language.objects.filter(studentID=student)]} for student in Student.objects.all()]
    # print(list(students))
    return render(request, 'manager/student_filter.html', {'nav':'manager','students':students})

@csrf_protect
def get_student_ID(request):
    studentID =Student.objects.all
    return HttpResponse(studentID)

@csrf_protect
def get_student_data(request):

    # lan =Language.objects.get().name
    # lan =Language.objects.filter(studentID="22221111").all().values_list('name')
    # template = loader.get_template('student_filter.html')
    # context = {
    #     'studentLan': lan,
    # }
    # print(context)
    # return HttpResponse(template.render(context, request))

    return HttpResponse(200)  
