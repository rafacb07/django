from django.conf.urls import patterns, url

from timesheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^employees/$', views.employees, name='employees_index'),
    url(r'employees/(\d?)/$', views.employee_detail, name='employee_detail'),
    url(r'^employees/create_employee/$', views.create_employee, name='create_employee'),
)