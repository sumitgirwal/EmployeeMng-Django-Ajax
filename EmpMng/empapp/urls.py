from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('office', views.officeCrud , name='office'),
    path('employee', views.employeeCrud , name='employee'),
    path('offices', views.offices , name='offices'),
    path('employees', views.employees , name='employees'),

    # path("pages/employee" , showEmployeePage),
    # path("pages/office" , showOfficePage)
]
