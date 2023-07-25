from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .models import *
import json
from django_base64field.fields import Base64Field
# Create your views here.

cv_list = [
    {"thumbnail":"/static/images/cv1.png","title":"Template-1","version":"cv_ui1"},
    {"thumbnail":"/static/images/cv2.png","title":"Template-2","version":"cv_ui2"},
    {"thumbnail":"https://cdn-images.zety.com/images/zety/landings/templates/enfold@1x.png","title":"Enfold"},
]


def dashboard(request):
    cvID= request.GET.get('cvID')
    return render(request, 'student/dashboard.html', {'nav':'student','cv_list':cv_list,'cvID':cvID})


def index(request):
    # cvID = request.GET.get('cvID')
    return render(request, 'student/index.html', {'nav': 'student'})


def cvForm(request):
    # cvID = request.GET.get('cvID')
    return render(request, 'student/createCvForm.html', {'nav': 'student'})


def jobList(request):
    # cvID = request.GET.get('cvID')
    return render(request, 'student/jobList.html', {'nav': 'student'})


def jobDetail(request):
    # cvID = request.GET.get('cvID')
    return render(request, 'student/jobDetail.html', {'nav': 'student'})

def studentProfile(request):
    # cvID = request.GET.get('cvID')
    return render(request, 'student/studentProfile.html', {'nav': 'student'})



def student_CV_UI(request):
    return render(request, 'student/cv.html', {'nav':'student'})

def student_CV_UI1(request):
    language=[]
    education=[]
    experience=[]
    cvBasic=[]

    cvID= request.GET.get('cvID')
    # student = Student.objects.get(user_id=request.user)
    cvBasic=CvInfoBase.objects.filter(cvId=cvID).values()

    for cvID in CvInfoBase.objects.filter(cvId=cvID):
         language = [lan for lan in Language.objects.filter(cv=cvID)]
         education = [edu for edu in Education.objects.filter(cv=cvID)]
         experience = [work for work in WorkExperience.objects.filter(cv=cvID)]
    
    return render(request, 'student/cv-version-1.html', {'nav':'student','cvBasic':cvBasic,'language':language,'education':education,'experience':experience})

def student_CV_UI2(request):
    language=[]
    education=[]
    experience=[]
    cvBasic=[]

    cvID= request.GET.get('cvID')
    # student = Student.objects.get(user_id=request.user)
    cvBasic=CvInfoBase.objects.filter(cvId=cvID).values()

    for cvID in CvInfoBase.objects.filter(cvId=cvID):
         language = [lan for lan in Language.objects.filter(cv=cvID)]
         education = [edu for edu in Education.objects.filter(cv=cvID)]
         experience = [work for work in WorkExperience.objects.filter(cv=cvID)]
    return render(request, 'student/cv-version-2.html', {'nav':'student','cvBasic':cvBasic,'language':language,'education':education,'experience':experience})

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
        #print(request.POST)

        new_cv = CvInfoBase(studentID=student,cvName=cvName,profileIcon=profileIcon,fristName=fristName,lastName=lastName,nickName=nickName,phone=phoneNumber,email=email,aboutMe=aboutMe)
        new_cv.save()
        
        for i in range(len(schoolNames)):
            if schoolNames[i] == '' or schoolNames[i] == None:
                continue
            education = Education(cv=new_cv, studentID=student,shcoolName=schoolNames[i],major=majoies[i],start_date=schoolStartDates[i], end_date=schoolEndDates[i])
            education.save()
        
        for i in range(len(companyNames)):
            if companyNames[i] == '':
                continue
            workExperience = WorkExperience(studentID=student,companyName=companyNames[i],start_date=companyStartDate[i],end_date=companyEndDate[i],description=description[i],cv=new_cv)
            workExperience.save()

        for i in languages:
            lan = Language(name=i, studentID=student)
            lan.save()
            lan.cv.add(new_cv)
            
      


        return JsonResponse({"status":True})
    return HttpResponseForbidden()


@csrf_exempt
@login_required
def edit_cvProfile(request):

    if request.method == "POST":
        cvID = request.POST.get('cv_id')

        cv = CvInfoBase.objects.get(cvId=cvID)
        cv.cvName = request.POST.get('cvName')
        cv.profileIcon = request.POST.get('profileIcon')
        cv.fristName = request.POST.get('fristName')
        cv.lastName = request.POST.get('lastName')
        cv.nickName = request.POST.get('nickName')
        cv.phone = request.POST.get('phoneNumber')
        cv.email = request.POST.get('email')
        cv.aboutMe = request.POST.get('aboutMe')
        cv.save()

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

        educations = Education.objects.filter(cv=cv).all()
        experiences = WorkExperience.objects.filter(cv=cv).all()

        for i in range(len(schoolNames)):
            if schoolNames[i] == '':
                continue
            try:
                education = educations[i]
                education.shcoolName = schoolNames[i]
                education.major = majoies[i]
                education.start_date = schoolStartDates[i]
                education.end_date = schoolEndDates[i]
                education.save()

            except:
                if schoolNames[i] != '':
                    education = Education(cv=cv, studentID=cv.studentID,shcoolName=schoolNames[i],major=majoies[i],start_date=schoolStartDates[i], end_date=schoolEndDates[i])
                    education.save()

        for i in range(len(companyNames)):
            if companyNames[i] == '':
                continue
            try:
                experiences[i].companyName = companyNames[i]
                experiences[i].description = description[i]
                experiences[i].start_date = companyStartDate[i]
                experiences[i].end_date = companyEndDate[i]
                experiences[i].save()
            except:
                if companyNames[i] != '':
                    workExperience = WorkExperience(studentID=cv.studentID,companyName=companyNames[i],start_date=companyStartDate[i],end_date=companyEndDate[i],description=description[i],cv=new_cv)
                    workExperience.save()


        #remove language records
        for l in Language.objects.filter(cv=cv).all():
            l.delete()

        for i in languages:
            if i != '':
                lan = Language(name=i, studentID=cv.studentID)
                lan.save()
                lan.cv.add(cv)


        return JsonResponse({"status":True})
    
    cvID = request.GET.get('cvID')
    language=[]
    education=[]
    experience=[]
    cvBasic=[]
    cvBasic=CvInfoBase.objects.filter(cvId=cvID).values()
    for cvID in CvInfoBase.objects.filter(cvId=cvID):
         language = [lan.name for lan in Language.objects.filter(cv=cvID)]
        #  education = [edu for edu in Education.objects.filter(cv=cvID)]
         education =  Education.objects.filter(cv=cvID).all()
         
         experience = [work for work in WorkExperience.objects.filter(cv=cvID)]

    educations = [edu.to_dict() for edu in list(education)]
    experiences = [exp.to_dict() for exp in experience]
    #     return JsonResponse({"status":True})
    return render(request, 'student/editProfile.html', {'nav':'student','cvID':request.GET.get('cvID'),'cvBasic':cvBasic,'languages':language,'educations':educations,'experiences':experiences})
    # return HttpResponseForbidden()


@csrf_exempt
@login_required
def delete_CV(request):
    if request.method == 'POST':
        request_JSON = json.loads(request.body)
        try:
            cv = CvInfoBase.objects.get(cvId=request_JSON["cv_id"])
            cv.delete()
            return JsonResponse({"status":True})
        except:
            
            return JsonResponse({"status":False})
        
    return HttpResponseForbidden()


def create_cv_form(request):
    return render(request, 'student/create_cv.html', {'nav':'student'})

@csrf_exempt
def create_new_cv(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        student = Student.objects.get(user_id=request.user.id)

        cv = CvInfoBase(studentID=student, cvName=json_data['cvName'], fristName=json_data['firstName'], lastName=json_data['lastName'], email=json_data['email'], phone=json_data['phone'], aboutMe=json_data['bio'])       
        cv.save()

        for education in json_data['educations']:
            edu = Education(studentID=student, shcoolName=education['institution'], major=education['program'], start_date=education['startDate'], end_date=education['endDate'])      
            edu.save()

        for workExp in json_data['workExperiences']:
            exp = WorkExperience(studentID=student, cv=cv, companyName=workExp['companyName'], description=workExp['description'], startDate=workExp['startDate'], endDate=workExp['endDate'])
            exp.save()
    
    return HttpResponseForbidden()