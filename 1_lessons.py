import csv
from dateutil import parser
import statistics
import pandas as pd
import datetime
Reis = 4
stop_1 = "1-Я И КАДЕТСКАЯ ЛИНИИ"
stop_2 = 'СЫТНЫЙ РЫНОК'
time_1 = None
time_2 = None
with open('task1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == stop_1:
            time_1 = row[4]
        if row[0] == stop_2:
            time_2 = row[4]
time_sum = parser.parse(time_2) - parser.parse(time_1)

list_1 = []
list_2 = []
list_3 = []
start = 0
start_1 = None
star_2 = None
star_3 = None
end = None
with open('task1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if start == 0 :
            start = 1
        elif start == 1:
            start_1 = parser.parse(row[1])
            start_2 = parser.parse(row[2])
            start_3 = parser.parse(row[3])
            start = 3
        else:
            list_1.append(parser.parse(row[1])-start_1)
            list_3.append(parser.parse(row[2])-start_2)
            list_2.append(parser.parse(row[3])-start_3)
            start_1 = parser.parse(row[1])
            start_2 = parser.parse(row[2])
            start_3 = parser.parse(row[3])

list_1_result = sum(list_1[8:13],datetime.timedelta())/len(list_1[8:13])
list_2_result = sum(list_2[8:13],datetime.timedelta())/len(list_2[8:13])
list_3_result = sum(list_3[8:13],datetime.timedelta())/len(list_3[8:13])
list_sum = [list_1_result,list_2_result,list_3_result]
list_sum = sum(list_sum,datetime.timedelta())
print(list_1_result)
print(list_2_result)
print(list_3_result)
print(time_sum)
print(list_sum)
time_1  = (list_1_result.total_seconds()*time_sum.total_seconds())/list_sum.total_seconds()
time_2  = (list_2_result.total_seconds()*time_sum.total_seconds())/list_sum.total_seconds()
time_3  = (list_3_result.total_seconds()*time_sum.total_seconds())/list_sum.total_seconds()
