# --*-- coding:utf8 --*--
from webtable.models import Production
from django.shortcuts import HttpResponseRedirect, Http404, HttpResponse, render_to_response, render

lists = []


def getdata():
    global lists
    lists = []
    records = Production.objects.all()
    # production.objects.

    n = 0
    for record in records:
        rec = {'Item_id': record.Item_id, 'Product_description': record.Product_description,  #eval(record.Product_description).decode('utf-8')
               'Part_Number': record.Part_Number,
               'Actual_capacity_until_eleven': record.Actual_capacity_until_eleven,
               'Planned_Capacity_per_day': record.Planned_Capacity_per_day,
               'Actual_capacity_until_thirteen': record.Actual_capacity_until_thirteen,
               'Actual_capacity_until_fiveteen': record.Actual_capacity_until_fiveteen,
               'Actual_capacity_until_thrty_to_eighteen': record.Actual_capacity_until_thrty_to_eighteen,
               'Actual_Capacity_per_day': record.Actual_Capacity_per_day,
               #'Scheduled_downtime_per_shirft': record.Scheduled_downtime_per_shirft,
               #'Unscheduled_downtime_lost_per_shirft': record.Unscheduled_downtime_lost_per_shirft,
               'Net_production_time_per_shift': record.Net_production_time_per_shift,
               'production_takt': record.production_takt, 'defective_products': record.defective_products,
               'Yield_Rate': record.Yield_Rate, 'Completion_ratio_per_shift': record.Completion_ratio_per_shift,
               'Attendance_due': record.Attendance_due, 'actual_attendence': record.actual_attendence}

        # print('数据库表中所有内容id：', record.Item_id)
        print('数据库表中所有内容Product_description：',  record.Product_description)   #eval(record.Product_description).decode('utf-8'))
        #print('数据库表中所有内容Part_Number：', record.Part_Number, type(record.Part_Number))
        # print('数据库表中所有内容：Planned_Capacity_per_day', record.Planned_Capacity_per_day)
        # print('数据库表中所有内容：Actual_capacity_until_eleven', record.Actual_capacity_until_eleven)
        # print('数据库表中所有内容：Actual_capacity_until_thirteen', record.Actual_capacity_until_thirteen)
        # print('数据库表中所有内容：', record.Actual_capacity_until_fiveteen)
        # print('数据库表中所有内容：', record.Actual_capacity_until_thrty_to_eighteen)
        # print('数据库表中所有内容：', record.Actual_Capacity_per_day)
        # print('数据库表中所有内容：', record.Scheduled_downtime_per_shirft)
        # print('数据库表中所有内容：', record.Unscheduled_downtime_lost_per_shirft)
        # print('数据库表中所有内容：', record.Net_production_time_per_shift)
        # print('数据库表中所有内容：', record.production_takt)
        # print('数据库表中所有内容：', record.defective_products)
        print('数据库表中所有内容：', record.Yield_Rate)
        print('数据库表中所有内容：', record.Completion_ratio_per_shift)
        # print('数据库表中所有内容：', record.Attendance_due)
        # print('数据库表中所有内容：', record.actual_attendence)
        lists.append(rec)
        n += 1
    # print('records in dataloader:', records)
    # print(lists)
    # return records
    # return render_to_response('login/productiondashboard.html', context={'records': records})
    # return render_to_response('login/productiondashboard.html', context={'lists': records})
    return lists


def show():
    global lists
    lists = []
    # if not lists:
    getdata()
    # print('debug lists in dataloader:',lists)
    return lists

    # return render_to_response('login/productiondashboard.html', context={'lists': lists})


if __name__ == '__main__':
    getdata()
    show()

