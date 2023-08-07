from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('company_information_page', views.company_information_page, name='company_information_page'),
    path('create_job_page', views.create_job_page, name='create_job_page'),
    #api
    path('create_company_api', views.create_company_api, name='create_company_api'),
    path('check_company_is_exists', views.is_company_exists, name='check_company_is_exists'),
    path('create_job_api', views.create_job_api, name="create_job_api")
]