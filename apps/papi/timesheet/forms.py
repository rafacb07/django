from django.forms import ModelForm
from timesheet.models import Employee, Employer

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['employer_id', 'name', 'lastname', 'email']

class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = ['name']