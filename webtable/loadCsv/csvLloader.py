# --*-- coding:utf8 --*--
from webtable.models import production
import xlrd


def loader(xlsx_file):
    file = xlrd.open_workbook(xlsx_file)
    # sheet = file.sheets()[0]
    sheet = file.sheet_by_index(0)

    # print("Worksheet name(s): {0}".format(file.sheet_names()))
    # print("Worksheet name:",sheet.name)
    # sheet = file.sheet_by_name(u'Sheet1')
    nrows = sheet.nrows
    ncols = sheet.ncols

    # print("{0} {1} {2}".format(sheet.name, sheet.nrows, sheet.ncols))

    # headers = [
    #             #'生产车间实时动态化管理看板',
    #            '序号\nItem',
    #            '产品描述\nProduct description',
    #            '产品型号\nPart Number',
    #            '计划产能\n（PCS/天）\nPlanned Capacity (PCS/Day) ',
    #            '实际产能状况Actual capacity Time Frame\n（时间段产能）',
    #            '实际产能\n（PCS/天）\nActual Capacity (PCS/Day)',
    #            '每班计划停机时间（小时）Scheduled downtime per shift',
    #            '每班非计划停机损失时间（小时）Unscheduled downtime lost per shift',
    #            '每班净生产时间\n(小时）Net production time per shift',
    #            '生产节拍\n（秒/件）production takt',
    #            '不良品\ndefective products',
    #            '良品率\nYield Rate',
    #            '每班达成率Completion ratio per shift',
    #            '应出勤人数Attendance due',
    #            '实际出勤人数actual attendence',
    #            ]

    #'Scheduled_downtime_per_shirft',
    #'Unscheduled_downtime_lost_per_shirft',

    headers = [
        'Product_description',
        'Part_Number',
        'Planned_Capacity_per_day',
        'Actual_capacity_until_eleven',
        'Actual_capacity_until_thirteen',
        'Actual_capacity_until_fiveteen',
        'Actual_capacity_until_thrty_to_eighteen',
        'Actual_Capacity_per_day',
        'Net_production_time_per_shift',
        'production_takt',
        'defective_products',
        'Yield_Rate',
        'Completion_ratio_per_shift',
        'Attendance_due',
        'actual_attendence',
    ]

    lists = []
    for row in range(6, sheet.nrows - 1):
        # for row in range(6,8):

        r = {}
        # print(row,' of ',nrows - 2, ' rows')
        for col in range(2, ncols):
            if not sheet.cell_value(rowx=row, colx=2):
                break
            else:
                # print(sheet.row_values(rowx=row))
                # print(col,' of ',ncols, ' cols')
                # print('col - 2:')
                key = headers[col - 2]
                # print('key:',key)
                if col == 2:
                    #r[key] = sheet.cell_value(rowx=row, colx=col).encode('utf-8')
                    r[key] = sheet.cell_value(rowx=row, colx=col)
                    #print('debug in csv loader', r[key])
                # elif col == 10:
                #
                #     r[key] = sheet.cell_value(rowx=row, colx=col)
                #     #print('debug in csv loader of col 10:', r[key])
                elif 4 <= col <= 12 and col != 10:
                    r[key] = float(sheet.cell_value(rowx=row, colx=col))
                    #print('debug in csv loader of col 4 - 12:', r[key])
                else:
                    r[key] = sheet.cell_value(rowx=row, colx=col)
                # print('r[key]:',key,r[key])
        if r:
            #print('debug in csv loader of r:', r)
            lists.append(r)

    # 首先，清空表
    production.objects.all().delete()

    sqllist = []
    for cell in lists:
        # for header in headers:
        Product_description = cell[headers[0]]
        Part_Number = cell[headers[1]]
        Planned_Capacity_per_day = cell[headers[2]]
        Actual_capacity_until_eleven = cell[headers[3]]
        Actual_capacity_until_thirteen = cell[headers[4]]
        Actual_capacity_until_fiveteen = cell[headers[5]]
        Actual_capacity_until_thrty_to_eighteen = cell[headers[6]]
        Actual_Capacity_per_day = cell[headers[7]]
        #Scheduled_downtime_per_shirft = cell[headers[8]]
        #Unscheduled_downtime_lost_per_shirft = cell[headers[9]]
        Net_production_time_per_shift = cell[headers[8]]
        production_takt = cell[headers[9]]
        defective_products = cell[headers[10]]
        Yield_Rate = cell[headers[11]]
        Completion_ratio_per_shift = cell[headers[12]]
        Attendance_due = cell[headers[13]]
        actual_attendence = cell[headers[14]]

        #print(Net_production_time_per_shift, production_takt)

        #product_description = Product_description.decode('utf-8')
        product_description = Product_description

        sql = production(Product_description=product_description, Part_Number=Part_Number,
                         Planned_Capacity_per_day=Planned_Capacity_per_day,
                         Actual_capacity_until_eleven=Actual_capacity_until_eleven,
                         Actual_capacity_until_thirteen=Actual_capacity_until_thirteen,
                         Actual_capacity_until_fiveteen=Actual_capacity_until_fiveteen,
                         Actual_capacity_until_thrty_to_eighteen=Actual_capacity_until_thrty_to_eighteen,
                         Actual_Capacity_per_day=Actual_Capacity_per_day,
                         Net_production_time_per_shift=Net_production_time_per_shift, production_takt=production_takt,
                         defective_products=defective_products, Yield_Rate=Yield_Rate,
                         Completion_ratio_per_shift=Completion_ratio_per_shift, Attendance_due=Attendance_due,
                         actual_attendence=actual_attendence)
                        #Scheduled_downtime_per_shirft=Scheduled_downtime_per_shirft,
                        #Unscheduled_downtime_lost_per_shirft=Unscheduled_downtime_lost_per_shirft,
        s = sql.save()

    #     sqllist.append(sql)
    #     print('debug in csv loader of sqlist:', sqllist)
    #     print('debug in csv loader of lists:', lists)
    # return sqllist
    #print('debug in csv loader of lists:', lists)
    return lists


if __name__ == '__main__':
    loader('../static/upload/LCD看板--生产块.xlsx')
