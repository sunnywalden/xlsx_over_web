#from __future__ import unicode_literals
import sys
from django.db import models
from django.contrib import admin

#sys.getdefaultencoding()

# Create your models here.


class Production(models.Model):
    Item_id = models.BigIntegerField(primary_key=True)
    Product_description = models.TextField()
    Part_Number = models.CharField(max_length=20)
    Planned_Capacity_per_day = models.BigIntegerField()
    Actual_capacity_until_eleven = models.BigIntegerField()
    Actual_capacity_until_thirteen = models.BigIntegerField()
    Actual_capacity_until_fiveteen = models.BigIntegerField()
    Actual_capacity_until_thrty_to_eighteen = models.BigIntegerField()
    Actual_Capacity_per_day = models.BigIntegerField()
    #Scheduled_downtime_per_shirft = models.FloatField()
    #Unscheduled_downtime_lost_per_shirft = models.FloatField()
    Net_production_time_per_shift = models.CharField(max_length=20)
    production_takt = models.BigIntegerField()
    defective_products = models.BigIntegerField()
    Yield_Rate = models.CharField(max_length=20)
    Completion_ratio_per_shift = models.CharField(max_length=20)
    Attendance_due = models.BigIntegerField()
    actual_attendence = models.BigIntegerField()


class User(models.Model):
    User_id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=40)
    Email = models.EmailField()
    Password = models.CharField(max_length=60)
    LoginStatus = models.BooleanField(default=False)
    LoginTime = models.DateTimeField()
