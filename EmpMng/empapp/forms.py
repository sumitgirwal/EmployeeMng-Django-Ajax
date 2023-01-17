from django import forms
from .models import Employee, Office

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'

