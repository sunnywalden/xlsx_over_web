# --*-- coding:utf8 --*--
import openpyxl

from webtable.models import Production
import xlrd


def loader(xlsx_file):
    try:
        workbook = openpyxl.load_workbook(xlsx_file, data_only=True)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        return data
    except Exception as e:
        print(f"Error loading xlsx file: {e}")
        return None


if __name__ == '__main__':
    loader('../static/upload/LCD看板--生产块.xlsx')
