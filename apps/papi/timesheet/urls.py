from django.conf.urls import patterns, url

from timesheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # Employee views
    url(r'^employees/$', views.employees, name='employees_index'),
    url(r'employees/(\d?)/$', views.employee_detail, name='employee_detail'),
    url(r'^employees/create_employee/$', views.create_employee, name='create_employee'),
    # Employer views
    url(r'^employers/$', views.employers, name='employers_index'),
    url(r'employers/(\d?)/$', views.employer_detail, name='employer_detail'),
    url(r'^employers/create_employer/$', views.create_employer, name='create_employer'),
    # Timesheet views
    url(r'^timesheets/$', views.timesheets, name='timesheets_index'),
    url(r'timesheets/(\d?)/$', views.timesheet_detail, name='timesheet_detail'),
    url(r'^timesheets/create_timesheet/$', views.create_timesheet, name='create_timesheet'),
)