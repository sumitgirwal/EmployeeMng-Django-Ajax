from django.shortcuts import render
from .models import Employee, Office
from .forms import EmployeeForm, OfficeForm
from django.http import JsonResponse

from django.core import serializers
# OR
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    context  = {
        'empform': EmployeeForm,
        'officeform': OfficeForm
    }
    return render(request, 'index.html', context)


def officeCrud(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            formre = form.save()
            context = {
                'msg':"Successfully Data Stored!!!"
            }
            # return JsonResponse(context, safe=False)
            # return JsonResponse(
            #     serializers.serialize("json", [form], safe=False)
            # )
            return JsonResponse(model_to_dict(formre), safe=False)
        else:
            context = {
                'error':form.errors
            }
            # return JsonResponse(
            #     serializers.serialize("json", [form.errors], safe=False)
            # )
            return JsonResponse(model_to_dict(form.errors), safe=False)

def employeeCrud(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            formre = form.save()
            context = {
                'msg':"Successfully Data Stored!!!"
            }
            return JsonResponse(model_to_dict(formre), safe=False)
        else:
            context = {
                'error':form.errors
            }
            return JsonResponse(model_to_dict(form.errors), safe=False)