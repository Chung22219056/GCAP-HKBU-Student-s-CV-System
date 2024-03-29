from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index', views.index, name='index'),
    path('cvForm', views.cvForm, name='cvForm'),
    path('jobList', views.jobList, name='jobList'),
    path('jobDetail', views.jobDetail, name='jobDetail'),
    path('studentProfile', views.studentProfile, name='studentProfile'),
    path('basicInfo', views.basicInfo, name='basicInfo'),
    path('checkLogin', views.checkLogin, name='checkLogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cv_ui', views.student_CV_UI, name='cv_ui'),
    path('cv_ui1', views.student_CV_UI1, name='cv_ui1'),
    path('cv_ui2', views.student_CV_UI2, name='cv_ui2'),
    path('cvProfile', views.student_cvProfile, name='cvProfile'),
    path('cvRecord', views.student_cvRecord, name='cvRecord'),
    path('create_cvProfile', views.create_cvProfile, name='create_cvProfile'),
    path('edit_cvProfile', views.edit_cvProfile, name='edit_cvProfile'),
    path('delete_cv', views.delete_CV, name='delete_CV'),
    path('create_cv_form', views.create_cv_form, name='create_cv_form'),
    path('create_new_cv', views.create_new_cv, name='create_new_cv'),
    path('edit_Cv', views.edit_Cv, name='edit_Cv'),
    path('getCvData', views.getCvData, name='getCvData'),
    path('getProfileData', views.getProfileData, name='getProfileData')
]
