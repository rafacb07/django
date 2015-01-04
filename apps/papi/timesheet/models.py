from django.db import models

# Create your models here.
class Timesheet(models.Model):
    employee_id = models.IntegerField(null=False, db_index=True)
    employer_id = models.IntegerField(null=False, db_index=True)
    report_date = models.DateTimeField('date published')
    hours       = models.IntegerField(null=False)
    flags       = models.IntegerField(null=False, db_index=True, default=0)

    class Meta:
        db_table = "timesheets"
        unique_together = ("employee_id", "report_date")

    def __str__(self):
        return str(self.id)


class Employee(models.Model):
    employer_id = models.IntegerField(null=False, db_index=True)
    name        = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    flags       = models.IntegerField(null=False, db_index=True, default=0)
    
    class Meta:
        db_table = "employees"
        unique_together = ("employer_id", "email")

    def __str__(self):
        return str(self.id)

    # Flags
    ACTIVE = 0x000001

    def isActive(self):
        return self.flags==ACTIVE

class Employer(models.Model):
    name        = models.CharField(max_length=255, unique=True)
    flags       = models.IntegerField(null=False, db_index=True, default=0)
    
    class Meta:
        db_table = "employers"

    def __str__(self):
        return str(self.id)