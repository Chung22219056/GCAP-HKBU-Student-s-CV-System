from django.urls import path
from . import views

urlpatterns = [
    path('index', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('students', views.students, name='students'),
    path('student_filter', views.student_filter, name='student_filter'),
    path('create_Job', views.create_Job, name='create_Job'),
    path('get_student_ID', views.get_student_ID, name='get_student_ID'),
    path('get_student_data', views.get_student_data, name='get_student_data'),
    path('send_email_to_student', views.send_email_to_student, name='send_email_to_student'),
    path('watch_student_CvRecord', views.watch_studentCvRecord, name='watch_student_CvRecord'),
    #API
    path('delete_student_api', views.delete_student_api, name='delete_student_api'),
    path('edit_student_api', views.edit_student_api, name='edit_student_api'),
    path('create_student_api', views.create_student_api, name='create_student_api'),
]