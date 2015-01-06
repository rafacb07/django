from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from timesheet.models import Employee, Employer, Timesheet
from timesheet.forms import EmployerForm
from timesheet.libraries.calendar import Calendar
import datetime

def timesheets(request):
    timesheets = Timesheet.objects.order_by('id')
    context = {'timesheets': timesheets}
    return render(request, 'timesheet/timesheets.html', context)

def timesheet_detail(request, timesheet_id):
    timesheet = Timesheet.objects.get(id=timesheet_id)
    context = {'timesheet': timesheet}
    return render(request, 'timesheet/timesheet_detail.html', context)

def create_timesheet(request):
    # Check if this is a post request or not
    if request.method == 'POST':
        # If post, create the form to create a new employer
        form = EmployerForm(request.POST)
        # Validation step
        if form.is_valid():
            # Create and save the new employer
            employer = form.save()
            employer.save()
            # Redirect to employer list page
            return redirect(employers)
        else:
            return render(request, 'timesheet/create_timesheet.html')
    else:
        calendar  = Calendar(datetime.datetime.now())
        week_days = calendar.get_week_days()
        context   = {'week_days': week_days}
        # If not a post request, show the form to create a new employer
        return render(request, 'timesheet/create_timesheet.html', context)