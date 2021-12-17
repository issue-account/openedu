import csv
import re
import os
import pandas as pd
from datetime import datetime, timedelta
from openpyxl.styles import Font, Fill
from openpyxl.utils import get_column_letter
import openpyxl
# List = ["<DATE>","<TIME>","<OPEN>","<HIGH>","<LOW>","<CLOSE>","<VOL>"]

OPEN = []
OPEN_result = []
CLOSE_result = []
CLOSE = []
HIGH = []
HIGH_result = []
LOW_result = []
LOW = []
time = {}
DATE= '13/09/18'
stop = 60
start = 0
time_start = 10
with open('task2-2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == DATE:
            OPEN.append(int(float(row[4])))
            CLOSE.append(int(float(row[7])))
            HIGH.append(int(float(row[5])))
            LOW.append(int(float(row[6])))

            if  int(str(row[3]).split(":")[0]) != time_start :
                print(str(row[3]).split(":")[0])
                OPEN_result.append(min(OPEN))
                CLOSE_result.append(max(CLOSE))
                HIGH_result.append(max(HIGH))
                LOW_result.append(min(LOW))
                OPEN  = []
                CLOSE = []
                start = 0
                time_start +=1
# from sklearn.metrics import r2_score
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# csv = pd.read_csv('SPFB_RTS-12_18_180901_181231_1_Karina.csv')
# data = csv[
# print(csv)
# print(data)

name_file='test-3'
report = openpyxl.Workbook()
sheet = report.active
len_time = 0
sheet.title = 'Отчет по проделоным задачам'
# таблица
style_font = Font(size=14,bold=True)
sheet['A1'].value = 'TIME'
sheet['A1'].font = style_font
sheet['B1'].value = 'OPEN'
sheet['B1'].font = style_font
sheet['C1'].value = 'HIGH'
sheet['C1'].font = style_font
sheet['D1'].value = 'LOW'
sheet['D1'].font = style_font
sheet['E1'].value = 'CLOSE'
sheet['E1'].font = style_font
# данные
for i in range(len(OPEN_result)):
    sheet[f'A{1+1+i}'].value = 11+i
    sheet[f'A{1+1+i}'].font  = Font(size=14)
    sheet[f'B{1+1+i}'].value = OPEN_result[i]
    sheet[f'B{1+1+i}'].font  = Font(size=14)
    sheet[f'C{1+1+i}'].value = HIGH_result[i]
    sheet[f'C{1+1+i}'].font  = Font(size=14)
    sheet[f'D{1+1+i}'].value = LOW_result[i]
    sheet[f'D{1+1+i}'].font  = Font(size=14)
    sheet[f'E{1+1+i}'].value = CLOSE_result[i]
    sheet[f'E{1+1+i}'].font  = Font(size=14)
report.save(f"./{name_file}.xlsx")
# # for i in range(len(OPEN_result)):
# #     print(OPEN_result[i]," ",HIGH_result[i]," ",LOW_result[i]," ",CLOSE_result[i]," ",)
