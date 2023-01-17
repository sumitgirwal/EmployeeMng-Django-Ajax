from django.contrib import admin
from .models import Employee, Office


# Register your models here.
admin.site.register(Office)
admin.site.register(Employee)
