from django.urls import path
from . import views

urlpatterns = [
    path('student_filter', views.student_filter, name='student_filter'),

    path('get_student_data', views.get_student_data, name='get_student_data')
]