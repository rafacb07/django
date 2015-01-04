from django.forms import ModelForm
from timesheet.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['employer_id', 'name', 'lastname', 'email']