from django.urls import path
from . import views

urlpatterns = [
    path('student_filter', views.student_filter, name='student_filter'),
    path('get_student_ID', views.get_student_ID, name='get_student_ID'),
    path('get_student_data', views.get_student_data, name='get_student_data'),
    path('send_email_to_student', views.send_email_to_student, name='send_email_to_student'),
]