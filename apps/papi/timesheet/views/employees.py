from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from timesheet.models import Employee, Employer, Timesheet
from timesheet.forms import EmployeeForm

def employees(request):
    employees = Employee.objects.order_by('-id')
    context = {'employees': employees}
    return render(request, 'timesheet/employees.html', context)

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    context = {'employee': employee}
    return render(request, 'timesheet/employee_detail.html', context)

def create_employee(request):
    # Check if this is a post request or not
    if request.method == 'POST':
        # If post, create the form to create a new employee
        form = EmployeeForm(request.POST)
        # Validation step
        if form.is_valid():
            # Create and save the new employee
            employee = form.save()
            employee.save()
            # Redirect to employee list page
            return redirect(employees)
        else:
            employers = Employer.objects.all()
            context = {
                'employers': employers,
                'error_message': 'The user could not be created (validation failed).'
            }
            return render(request, 'timesheet/create_employee.html', context)
    else:
        # If not a post request, show the form to create a new employee
        employers = Employer.objects.all()
        context = {'employers': employers}
        return render(request, 'timesheet/create_employee.html', context)