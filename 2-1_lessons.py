import csv
import re
import os
from datetime import datetime, timedelta
from openpyxl.styles import Font, Fill
from openpyxl.utils import get_column_letter
import openpyxl
DATE      = '16.12.2020'
TIME      = '16:52:00'
TOTAL_SUM = 0
TOTAL     = 0
PRICE     = 0
with open('task2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == DATE  and row[1] == TIME :
            # print(row)113570 115292 108141 108610
            sum = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
            PRICE = sum/4
print("PRICE = ", PRICE)
DATE = '10.09.2020'
TIME = '19:50:00'
TOTAL_SUM = 0
TOTAL = 0
PRICE = 0
with open('task2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == DATE  and row[1] == TIME :
            # print(row)113570 115292 108141 108610
            sum = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
            PRICE = sum/4
            TOTAL = PRICE * float(row[6])
print("TOTAL = ", TOTAL)
DATE = '01.10.2020'
TOTAL_SUM = 0
TOTAL = 0

PRICE = 0
with open('task2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader      :
        if row[0] == DATE  :
            # print(row)113570 115292 108141 108610
            sum = float(row[2]) + float(row[3]) + float(row[4]) + float(row[5])
            PRICE = sum/4
            TOTAL = PRICE * float(row[6])
            TOTAL_SUM +=TOTAL
print("TOTAL_SUM = ", TOTAL_SUM)

TIME = "08.12.2020"
Counter=0
with open('task2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == TIME : # and row[1] == TIME :
            # print(row)
            if row[2] >= row[5]:
                Counter+=1
print("Counter", Counter)

Wednesday=['03','10','17','24']
DATE= [i+".11.2020" for i in Wednesday ]
print(DATE)
TOTAL_SUM = 0
with open('task2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in DATE : # and row[1] == TIME :
            PRICE = (int(row[2]) + int(row[3]) + int(row[4]) + int(row[5]))/4
            TOTAL = PRICE * int(row[6])
            TOTAL_SUM +=TOTAL
print(round(TOTAL_SUM))
