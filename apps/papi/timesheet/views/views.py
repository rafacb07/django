from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from timesheet.models import Employee, Employer, Timesheet


def index(request):
    employees  = Employee.objects.order_by('id')
    employers  = Employer.objects.order_by('id')
    timesheets = Timesheet.objects.raw('Select t.id, t.report_date, e.name from timesheets as t, employees as e where t.employee_id=e.id order by id asc')

    context = {
    	'employees': employees,
    	'employers': employers,
    	'timesheets': timesheets
    }
    
    return render(request, 'timesheet/index.html', context)