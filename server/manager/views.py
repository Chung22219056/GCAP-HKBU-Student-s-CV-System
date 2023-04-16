from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect
from student.models import *
import json
from function.email import sendEmail

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


@csrf_protect
def send_email_to_student(request):
    try:
        json_data = json.loads(request.body)
        student_id = json_data['student_id']
        email_content = json_data['email_content']

        if student_id == 'all':
            pass
        else:
            student = Student.objects.get(student_id=student_id)
            print(email_content)
            sendEmail(student.user_id.email, email_content)
        
        return JsonResponse({'status': True})
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})

