from django.urls import path
from . import views

urlpatterns = [
    path('cv_ui', views.student_CV_UI, name='cv_ui'),
    path('cv_ui1', views.student_CV_UI1, name='cv_ui1'),
    path('cv_ui2', views.student_CV_UI2, name='cv_ui2'),
     path('profile', views.student_Profile, name='profile'),
]
