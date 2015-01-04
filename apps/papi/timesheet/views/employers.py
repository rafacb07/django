from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from timesheet.models import Employee, Employer, Timesheet
from timesheet.forms import EmployerForm

def employers(request):
    employers = Employer.objects.order_by('id')
    context = {'employers': employers}
    return render(request, 'timesheet/employers.html', context)

def employer_detail(request, employer_id):
    employer = Employer.objects.get(id=employer_id)
    context = {'employer': employer}
    return render(request, 'timesheet/employer_detail.html', context)

def create_employer(request):
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
            return render(request, 'timesheet/create_employer.html')
    else:
        # If not a post request, show the form to create a new employer
        return render(request, 'timesheet/create_employer.html')