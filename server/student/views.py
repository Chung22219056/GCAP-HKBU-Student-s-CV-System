from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
def create_cvProfile(request):
    print("asd")
    if request.method=='POST':
        fristName = request.POST.get('fristName')
        print(fristName)
        # return JsonResponse({"status":fristName})
      
    
    # return JsonResponse(request.POST.get('fristName'))
    return render(request, 'student/cvProfile')

