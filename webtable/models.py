from __future__ import unicode_literals
import sys
from django.db import models
from django.contrib import admin

sys.getdefaultencoding()

# Create your models here.
class production(models.Model):
    #Item = models.AutoField()
    Product_description = models.TextField()
    Part_Number = models.CharField(max_length=20)
    Planned_Capacity_per_day = models.FloatField()
    Actual_capacity_until_eleven = models.FloatField()
    Actual_capacity_until_thirteen = models.FloatField()
    Actual_capacity_until_fiveteen = models.FloatField()
    Actual_capacity_until_thrty_to_eighteen = models.FloatField()
    Actual_Capacity_per_day = models.FloatField()
    #Scheduled_downtime_per_shirft = models.FloatField()
    #Unscheduled_downtime_lost_per_shirft = models.FloatField()
    Net_production_time_per_shift = models.CharField(max_length=20)
    production_takt = models.BigIntegerField()
    defective_products = models.BigIntegerField()
    Yield_Rate = models.CharField(max_length=20)
    Completion_ratio_per_shift = models.CharField(max_length=20)
    Attendance_due = models.BigIntegerField()
    actual_attendence = models.BigIntegerField()
