import csv

# 1 task
Region = []
Cname = []
Year = []
Number_of_cases = []
test = 0
Cname_search = 'Madagascar'
with open('final-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if test != 0:
            time = row[0].split(";")
            if time[1] == Cname_search:
                print(1)
                Region.append(time[0])
                Cname.append(time[1])
                Year.append(time[2])
                Number_of_cases.append(int(time[3]) if time[3] !='' else 0)
        else:
            test=1
import os
from openpyxl.styles import Font, Fill
from openpyxl.utils import get_column_letter
import openpyxl

name_file='final-1-answer'
report = openpyxl.Workbook()
sheet = report.active
len_time = 0
sheet.title = 'Отчет по проделоным задачам'
# таблица
style_font = Font(size=14,bold=True)
sheet['A1'].value = 'Region'
sheet['A1'].font = style_font
sheet['B1'].value = 'Cname'
sheet['B1'].font = style_font
sheet['C1'].value = 'Year'
sheet['C1'].font = style_font
sheet['D1'].value = 'Number of cases'
# данные
for i in range(len(Region)):
    sheet[f'A{1+1+i}'].value = Region[i]
    sheet[f'A{1+1+i}'].font  = Font(size=14)
    sheet[f'B{1+1+i}'].value = Cname[i]
    sheet[f'B{1+1+i}'].font  = Font(size=14)
    sheet[f'C{1+1+i}'].value = Year[i]
    sheet[f'C{1+1+i}'].font  = Font(size=14)
    sheet[f'D{1+1+i}'].value = Number_of_cases[i]
    sheet[f'D{1+1+i}'].font  = Font(size=14)
report.save(f"./{name_file}.xlsx")
