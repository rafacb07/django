# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer_id', models.IntegerField(db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('flags', models.IntegerField(default=0, db_index=True)),
            ],
            options={
                'db_table': 'employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('flags', models.IntegerField(default=0, db_index=True)),
            ],
            options={
                'db_table': 'employers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_id', models.IntegerField(db_index=True)),
                ('employer_id', models.IntegerField(db_index=True)),
                ('report_date', models.DateTimeField(verbose_name=b'date published')),
                ('hours', models.IntegerField()),
                ('flags', models.IntegerField(default=0, db_index=True)),
            ],
            options={
                'db_table': 'timesheets',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='timesheet',
            unique_together=set([('employee_id', 'report_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([('employer_id', 'email')]),
        ),
    ]
