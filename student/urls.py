from django.urls import path
from . import views

urlpatterns = [
    path('cv_ui', views.student_CV_UI, name='cv_ui'),
]
