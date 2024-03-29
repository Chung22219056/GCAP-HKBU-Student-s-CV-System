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

@csrf_exempt
@login_required
def basicInfo(request):
    # cvID = request.GET.get('cvID')
    if request.method == 'POST':
        request_JSON = json.loads(request.body)
        # print(request_JSON)
        
        student = Student.objects.get(user_id=request.user.id)
        # print(student)
        newCvInfoBasic =CvInfoBase(studentID=student,profileIcon=request_JSON["profileIcon"],fristName=request_JSON["fristName"],lastName=request_JSON["lastName"],nickName=request_JSON["nickName"],phone=request_JSON["phoneNumber"],email=request_JSON["email"],aboutMe=request_JSON["aboutMe"])
        newCvInfoBasic.save()
        return JsonResponse({"status":True})
        
    return render(request, 'student/basicInfo.html', {'nav': 'student'})


def checkLogin(request):
    cvID = request.GET.get('cvID')
    cv = CvInfoBase.objects.filter(studentID=Student.objects.get(user_id=request.user.id)).values()
    isCvEmpty = False
    if(cv.count() == 0):
        isCvEmpty = True
    # print(cv)
    return render(request, 'student/checkLogin.html', {'nav': 'student','cv':cv, "isCvEmpty": isCvEmpty})



def student_CV_UI(request):
    return render(request, 'student/cv.html', {'nav':'student'})

def student_CV_UI1(request):
    language=[]
    skill=[]
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
         skill = [skill for skill in Skill.objects.filter(cv=cvID)]
         print(skill)
    
    return render(request, 'student/cv-version-1.html', {'nav':'student','cvBasic':cvBasic,'language':language,'skill':skill,'education':education,'experience':experience})

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
         skill = [skill for skill in Skill.objects.filter(cv=cvID)]
         education = [edu for edu in Education.objects.filter(cv=cvID)]
         experience = [work for work in WorkExperience.objects.filter(cv=cvID)]
    return render(request, 'student/cv-version-2.html', {'nav':'student','cvBasic':cvBasic,'language':language,'skills':skill,'education':education,'experience':experience})

@csrf_exempt
@login_required
def student_cvProfile(request):
    
    studentProfile = Student.objects.filter(user_id=request.user).values()
    user = User.objects.filter(id=request.user.id)
    if request.method == 'POST':
        request_JSON = json.loads(request.body)

    
        editStudent = Student.objects.get(user_id=request.user.id)
        # print(editStudent.email)
        editStudent.profileIcon = request_JSON["profileIcon"]
        editStudent.nickName = request_JSON["nickName"]
        editStudent.phone = request_JSON["phoneNumber"]
        editStudent.aboutMe = request_JSON["aboutMe"]
        editStudent.save()
        

        editUser = User.objects.get(id=request.user.id)
        print(editUser.email)
        editUser.first_name = request_JSON["fristName"]
        editUser.last_name = request_JSON["lastName"]
        editUser.email = request_JSON["email"]
        editUser.save()
        
        return JsonResponse({"status":True})
    return render(request, 'student/cvProfile.html', {'nav':'student','studentProfile':studentProfile,'user':user})

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
    # print(request.POST.get('cv_id'))
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
            print(CvInfoBase.objects.all())
            cv = CvInfoBase.objects.filter(cvId=request_JSON["cv_id"])
            cv.delete()
            return JsonResponse({"status":True})
        except:
            return JsonResponse({"status":False}) 
    return HttpResponseForbidden()


@csrf_exempt
@login_required
def create_cv_form(request):
    # print(request.method)
    # if request.method =="GET":
    #     studentProfile = Student.objects.filter(user_id=request.user).values()
    #     # print(studentProfile)
    #     user = User.objects.filter(id=request.user.id)
    #     # print(list(studentProfile))
    #     return JsonResponse(list(studentProfile), safe=False) 
    
    return render(request, 'student/create_cv.html', {'nav':'student'})


def getProfileData(request):
    #  print(request.method)
     profileData=[]
     if request.method =="GET":
        
        studentProfile = Student.objects.filter(user_id=request.user).values()
        for i in studentProfile:
         profileData.append(i)

        user = User.objects.filter(id=request.user.id).values()
        for user in user:
         profileData.append(user)
        return JsonResponse(list(profileData), safe=False) 



@csrf_exempt
def create_new_cv(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            student = Student.objects.get(user_id=request.user.id)
            lan = Language.objects.all()
            print(json_data)  
            # print(json_data['base64ImgProfileIcon'])

            cv = CvInfoBase(studentID=student, cvName=json_data['cvName'],fristName=json_data['firstName'], lastName=json_data['lastName'], nickName=json_data['nickName'],email=json_data['email'], phone=json_data['phone'], aboutMe=json_data['bio'], profileIcon=json_data['base64ImgProfileIcon'])       
            cv.save()

            for education in json_data['educations']:
                edu = Education(studentID=student, cv=cv, shcoolName=education['institution'], major=education['program'], start_date=education['startDate'], end_date=education['endDate'])      
                edu.save()

            for workExp in json_data['workExperiences']:
                exp = WorkExperience(studentID=student, cv=cv, companyName=workExp['companyName'], description=workExp['description'], start_date=workExp['startDate'], end_date=workExp['endDate'])
                exp.save()
                
            for language in json_data['languages']:
                lan = Language(studentID=student, cv=cv,name=language)
                lan.save()
            
            for skill in json_data['skills']:
                skill = Skill(cv=cv,studentID=student,name=skill)
                skill.save()
            
            return JsonResponse({"status":True})
        except Exception as e:
            print(e)
            return JsonResponse({"status":False})
    
    return HttpResponseForbidden()


@csrf_exempt
@login_required
def edit_Cv(request):
    cvID = request.GET.get('cvID')
    # print(cvID)
    language=[]
    education=[]
    experience=[]
    skill=[]
    cvBasic=[]
    cvBasic=CvInfoBase.objects.filter(cvId=cvID).values()

   
    for cv in CvInfoBase.objects.filter(cvId=cvID):
        language = [lan.name for lan in Language.objects.filter(cv=cv)]
        skill = [skill for skill in Skill.objects.filter(cv=cv)]
        education = [edu for edu in Education.objects.filter(cv=cv)]
        experience = [work for work in WorkExperience.objects.filter(cv=cv)]

    educations = [edu.to_dict() for edu in education]
 
    experiences = [exp.to_dict() for exp in experience]
    


    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            cv = CvInfoBase.objects.get(cvId=json_data.get('cvID'))
     
            
            # Cv Basic
            cv.profileIcon = json_data['base64ImgProfileIcon']      
            cv.cvName = json_data['cvName']
            cv.fristName = json_data['firstName']
            cv.lastName = json_data['lastName']
            cv.nickName = json_data['nickName']
            cv.email = json_data['email']
            cv.aboutMe = json_data['bio']
            cv.phone = json_data['phone']
            cv.save()
            
            #Education
            education = Education.objects.filter(cv=cv).all()
            getRequestEdu = json_data['educations']
            getRequestWork = json_data['workExperiences']
            getRequestLan = json_data['languages']
            getRequestSkill = json_data['skills']
    
            #  remove education records
            # add new education records
            for edu in education:
                edu.delete()
      
            for edu in range(len(getRequestEdu)):
                education = Education(studentID=cv.studentID, cv=cv, shcoolName=getRequestEdu[edu]['institution'], major=getRequestEdu[edu]['program'], start_date=getRequestEdu[edu]['startDate'], end_date=getRequestEdu[edu]['endDate'])      
                education.save()
                
            # Edit WorkExperience
            for work in WorkExperience.objects.filter(cv=cv).all():
                work.delete()
                
            for work in range(len(getRequestWork)):
                workExperience = WorkExperience(studentID=cv.studentID, cv=cv, companyName=getRequestWork[work]['companyName'], description=getRequestWork[work]['description'], start_date=getRequestWork[work]['startDate'], end_date=getRequestWork[work]['endDate'])
                workExperience.save()
                
            #Edit Language
            for lan in Language.objects.filter(cv=cv).all():
                lan.delete()
                
            for lan in getRequestLan:
                print(lan)
                lan = Language(studentID=cv.studentID, cv=cv,name=lan)
                lan.save()
                
            
            #Edit Skill 
            for skill in Skill.objects.filter(cv=cv).all():
                skill.delete()
                
            for skill in getRequestSkill:
                skill = Skill(cv=cv,studentID=cv.studentID,name=skill)
                skill.save()
            
        

            return JsonResponse({"status":True})
        except Exception as e:
            print(e)
            return JsonResponse({"status":False})
      
  

    return render(request, 'student/edit_cv.html',{'nav':'student','cvBasic':cvBasic,'skills':skill,'languages':language,'education':educations,'experience':experiences})


@csrf_exempt
@login_required
def getCvData(reqest):
    print(reqest.method)
    if reqest.method =="POST":
        print(reqest.POST)
        return JsonResponse(list(reqest), safe=False) 
        # return jsonify(reqest)

