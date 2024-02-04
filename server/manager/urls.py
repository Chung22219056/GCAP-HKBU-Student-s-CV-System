from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('dashboard', views.index, name='index'),
    path('accounts', views.accounts, name='accounts'),
    path('jobs', views.jobs, name='jobs'),
]