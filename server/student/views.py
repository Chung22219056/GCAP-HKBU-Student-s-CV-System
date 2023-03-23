from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .models import *
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

def student_cvRecord(request):
    student = Student.objects.get(user_id=request.user)
    cv_list = CvInfoBase.objects.filter(studentID=student)
    return render(request, 'student/cvRecord.html', {'nav':'student','cv_list':cv_list})

@csrf_exempt
@login_required
def create_cvProfile(request):
    if request.method=='POST':
        student = Student.objects.get(user_id=request.user.id)
        fristName = request.POST.get('fristName')
        lastName = request.POST.get('lastName')
        nickName = request.POST.get('nickName')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        aboutMe = request.POST.get('aboutMe')

        schoolNames = request.POST.getlist('schoolNames[]')
        majoies = request.POST.getlist('majors[]')

        new_cv = CvInfoBase(studentID=student,fristName=fristName,lastName=lastName,nickName=nickName,phone=phoneNumber,email=email,aboutMe=aboutMe)
        new_cv.save()
        
        #save education data
        for i in range(len(majoies)):
            education = Education(studentID=student,shcoolName=schoolNames[i],major=majoies[i],cv=new_cv)
            education.save()

        return JsonResponse({"status":True})
    return HttpResponseForbidden()

