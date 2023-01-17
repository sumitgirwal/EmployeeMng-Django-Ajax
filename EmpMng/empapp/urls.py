from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('office', views.officeCrud , name='office'),
    path('employee', views.employeeCrud , name='employee'),
]
