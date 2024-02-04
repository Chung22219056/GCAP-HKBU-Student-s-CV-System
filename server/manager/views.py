from django.shortcuts import render
from student.models import *

# Create your views here.
def index(request):
    numOfStudent = len(Student.objects.all())
    numOfCv = len(CvInfoBase.objects.all())
    return render(request, 'manager/dashboard.html', {'numOfStudent': numOfStudent, 'numOfCv': numOfCv})


def accounts(request):
    students = [student.toDict() for student in Student.objects.all()]
    return render(request, 'manager/accounts.html', {'students': students})

def jobs(request):
    return render(request, 'manager/jobs.html')
