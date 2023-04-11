from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .models import *
from django_base64field.fields import Base64Field
# Create your views here.

cv_list = [
    {"thumbnail":"https://cdn-images.zety.com/images/zety/landings/templates/cascade@1x.png","title":"Cascade"},
    {"thumbnail":"https://cdn-images.zety.com/images/zety/landings/templates/crisp@1x.png","title":"Crisp"},
    {"thumbnail":"https://cdn-images.zety.com/images/zety/landings/templates/enfold@1x.png","title":"Enfold"},
    
]

def dashboard(request):
    return render(request, 'student/dashboard.html', {'nav':'student','cv_list':cv_list})

def student_CV_UI(request):
    return render(request, 'student/cv.html', {'nav':'student'})

def student_CV_UI1(request):
    return render(request, 'student/cv-version-1.html', {'nav':'student'})

def student_CV_UI2(request):
    return render(request, 'student/cv-version-2.html', {'nav':'student'})

def student_cvProfile(request):
    return render(request, 'student/cvProfile.html', {'nav':'student'})

@login_required
def student_cvRecord(request):
    # only for logged user
    student = Student.objects.get(user_id=request.user)
    studentLan = [{'language':[lan.name for lan in Language.objects.filter(studentID=student)]} for student in Student.objects.all()]
    cv_list = CvInfoBase.objects.filter(studentID=student)
    return render(request, 'student/cvRecord.html', {'nav':'student','cv_list':cv_list})

@csrf_exempt
@login_required
def create_cvProfile(request):
    if request.method=='POST':
        student = Student.objects.get(user_id=request.user.id)
        # print(request.POST)
        cvName=request.POST.get('cvName')
        profileIcon=request.POST.get('profileIcon')
        fristName = request.POST.get('fristName')
        lastName = request.POST.get('lastName')
        nickName = request.POST.get('nickName')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        aboutMe = request.POST.get('aboutMe')

        # Education
        schoolNames = request.POST.getlist('schoolNames[]')
        majoies = request.POST.getlist('majors[]')
        languages = request.POST.getlist('language[]')
        schoolStartDates = request.POST.getlist('schoolStartDates[]')
        schoolEndDates = request.POST.getlist('schoolEndDates[]')

        #WorkExperience
        companyNames=request.POST.getlist('companyNames[]')
        companyStartDate = request.POST.getlist('companyStartDate[]')
        companyEndDate = request.POST.getlist('companyEndDate[]')
        description=request.POST.getlist('description[]')


        new_cv = CvInfoBase(studentID=student,cvName=cvName,profileIcon=profileIcon,fristName=fristName,lastName=lastName,nickName=nickName,phone=phoneNumber,email=email,aboutMe=aboutMe)
        new_cv.save()
        
        # # save education data
        # for i in range(len(majoies)):
        #    education = Education(studentID=student,shcoolName=schoolNames[i],major=majoies[i],start_date=schoolStartDates[i],end_date=schoolEndDates[i],cv=new_cv)
        #    education.save()

        # save work experiences data
        for i in range(len(companyNames)):
            print("errorsssssssssssssssssss")
            # print(i)
            workExperience = WorkExperience(studentID=student,companyName=companyNames[i],start_date=companyStartDate[i],end_date=companyEndDate[i],description=description[i],cv=new_cv)
            workExperience.save()



        # #save language
        for i in languages:
            lan = Language(name=i, studentID=student)
            lan.save()
            lan.cv.add(new_cv)

        return JsonResponse({"status":True})
    return HttpResponseForbidden()




