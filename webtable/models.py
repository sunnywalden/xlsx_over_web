#from __future__ import unicode_literals
import sys
from django.db import models
from django.contrib import admin

#sys.getdefaultencoding()

# Create your models here.


class Production(models.Model):
    item_id = models.BigIntegerField(primary_key=True)
    product_description = models.TextField()
    part_number = models.CharField(max_length=20)
    planned_capacity_per_day = models.BigIntegerField()
    actual_capacity_until_eleven = models.BigIntegerField()
    actual_capacity_until_thirteen = models.BigIntegerField()
    actual_capacity_until_fiveteen = models.BigIntegerField()
    actual_capacity_until_thrty_to_eighteen = models.BigIntegerField()
    actual_Capacity_per_day = models.BigIntegerField()
    #Scheduled_downtime_per_shirft = models.FloatField()
    #Unscheduled_downtime_lost_per_shirft = models.FloatField()
    net_production_time_per_shift = models.CharField(max_length=20)
    production_takt = models.BigIntegerField()
    defective_products = models.BigIntegerField()
    yield_rate = models.CharField(max_length=20)
    completion_ratio_per_shift = models.CharField(max_length=20)
    attendance_due = models.BigIntegerField()
    actual_attendence = models.BigIntegerField()


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    login_status = models.BooleanField(default=False)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username