from django.shortcuts import render, HttpResponse
from django.http import HttpResponseForbidden, JsonResponse
from .models import *
import json

# Create your views here.
def index(request):
    return render(request, 'employer/index.html')

def company_information_page(request):
    return render(request, 'employer/conpany_information_page.html')

def create_job_page(request):
    return render(request, 'employer/create_job_page.html')

def is_company_exists(request):
    name = request.GET.get('company_name')
    company = CompanyInformation.objects.filter(company_name=name)
    return JsonResponse({'exists': (len(company) > 0) })

def create_company_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            company = CompanyInformation(
                contact_person= data['contact_person'],
                email = data['email'],
                phone = data['phone'],
                company_name = data['company_name'],
                website = data['website'],
            )

            #company.save()
            
            return JsonResponse({'status': True})
        except Exception as e:
            return JsonResponse({'status': False})
    return HttpResponseForbidden()

def create_job_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company = CompanyInformation.objects.find(company_name=data['company_name'])

        job = Job(
            title = data['title'],
            start_date = data['start_date'],
            duration = data['duration'],
            salary = data['salary'],
            job_requirement = data['job_requirement'],
            job_description = data['job_description'],
            application_method = data['application_method'],
            remarks = data['remarks'],
            company_id = company
        )

        #job.save()
        return JsonResponse({'status': True})
    return HttpResponseForbidden()
