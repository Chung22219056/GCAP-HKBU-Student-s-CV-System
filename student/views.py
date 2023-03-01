from django.shortcuts import render, HttpResponse

# Create your views here.
def student_CV_UI(request):
    return render(request, 'student/cv.html', {'nav':'student'})