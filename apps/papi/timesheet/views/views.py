from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from timesheet.models import Employee, Employer, Timesheet


def index(request):
    employees = Employee.objects.order_by('-id')
    employers = Employer.objects.order_by('-id')
    timesheets = Timesheet.objects.order_by('-id')

    context = {
    	'employees': employees,
    	'employers': employers,
    	'timesheets': timesheets
    }
    
    return render(request, 'timesheet/index.html', context)