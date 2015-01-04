from django.contrib import admin
from timesheet.models import Timesheet, Employee, Employer

# Register your models here.
admin.site.register(Timesheet)
admin.site.register(Employer)
admin.site.register(Employee)