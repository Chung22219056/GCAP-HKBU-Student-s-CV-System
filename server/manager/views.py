from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import requires_csrf_token,csrf_protect,csrf_exempt
from student.models import *
import json
from function.email import sendEmail
from django.http import HttpResponseForbidden

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
            students = Student.objects.all()
            for student in students:
                sendEmail(student.user_id.email, email_content)
        else:
            student = Student.objects.get(student_id=student_id)
            print(email_content)
            sendEmail(student.user_id.email, email_content)
        
        return JsonResponse({'status': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'status': False})

def watch_studentCvRecord(request):
    # only for logged user
    stud_id= request.GET.get('studentID')
    print(stud_id)
    student = Student.objects.get(student_id=stud_id)
    studentLan = [{'language':[lan.name for lan in Language.objects.filter(studentID=student)]} for student in Student.objects.all()]
    cv_list = CvInfoBase.objects.filter(studentID=student)
    return render(request, 'manager/watchStudentCvRecord.html', {'nav':'manager','cv_list':cv_list})


def dashboard(request):
    return render(request, "manager/dashboard.html")

# @csrf_protect
@csrf_exempt
def create_Job(request):
    email=[]
    # if request.method=='POST':
    student = Student.objects.all()
    users = User.objects.all()
   
    for user in users:
        student = Student.objects.filter(user_id=user)
        for stu in student:
           studentCv = CvInfoBase.objects.filter(studentID=stu)
           for cv in studentCv:
               for language in request.POST.getlist('lan[]'):
                programLan = Language.objects.filter(cv=cv).filter(name=language)
                for lan in programLan:
                    if user.email not in email:
                        sendEmail(user.email, request.POST.get("jobDescription"))
                        email.append(user.email)
                    else:
                        continue

    
  
    #   print(request.POST)
    return render(request, "manager/createJob.html", {'nav':'manage'})

