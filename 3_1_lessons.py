import math
import csv
import operator

ID,DISTANCE,STOP_COUNT,COST = [],[],[],[]
Normirovka = {}
test = 0

def func_exp(x,min):
    return 1-math.exp(1-(x/min))

with open('task3-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if test != 0:
            ID.append(row[0])
            DISTANCE.append(int(row[1]))
            STOP_COUNT.append(int(row[2]))
            COST.append(float(row[3]))
        else:
            test=1

for i in range(len(ID)):
    Normirovka[i+1] = func_exp(DISTANCE[i],min(DISTANCE))+func_exp(STOP_COUNT[i], min(STOP_COUNT))+func_exp(COST[i],min(COST))
print("List = ",sorted(Normirovka.items(), key=operator.itemgetter(1))[:3])
