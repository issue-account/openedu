import csv
import math
# 1 task
Subject_RF = []
Okrug = 'Северо-Западный'
with open('final2-2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == Okrug:
            Subject_RF.append(row[0])

# 2 task
year_electro = []
period_electro = []
i = 0
j = 0
a = 0
test = 0
with open('final2-1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in Subject_RF:
            year_electro.append(float(row[a]))
            p = 0
            for x in range(i,j+1):
                p += float(row[x])
            period_electro.append(p)
        else:
            if test == 0:
                a = row.index('2007')
                i = row.index('2000')
                j = row.index('2010')
                test = 1
print("year = ",round(sum(year_electro),1))
print("period year = ",round(sum(period_electro),1))
# 3 task
#Y = [33,46,52,39,40,51,50,44,53,48,57,60,59,47,56,49,54,68,69,62,65,64,66,55,73]
Y = [40, 43, 52, 44, 47, 39, 50, 54, 45, 41, 58, 56,
     63, 64, 57, 49, 48, 51, 66, 60, 61, 65, 62, 59, 75]


def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det

a,b = linreg(range(len(Y)),Y)  #your x,y are switched from standard notation
print( "a =",  round(a,2))
def X_t(x):
    return sum(x)/len(x)
def R2(x, y, Q1, Q0):
    m = sum([(i-X_t(y))**2 for i in y])
    t = sum([(j-Q0-Q1*i)**2 for i, j in zip(x, y)])
    return 1-(t/m)
R_2 = R2(range(len(Y)), Y, a, b)
print("R2 = ", round(R_2, 3))

# 4 task
ID = []
GUESTS = []
INCOME = []
STARS = []
test = 0
with open('final3.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if test != 0:
            ID.append(row[0])
            GUESTS.append(int(row[1]))
            INCOME.append(int(row[2]))
            STARS.append(int(row[3]))
        else:
            test=1
GUESTS_min = min(GUESTS)
INCOME_min = min(INCOME)
STARS_min = min(STARS)
GUESTS_max = max(GUESTS)
INCOME_max = max(INCOME)
STARS_max = max(STARS)
list_restarunt = {}
guests_x = []


def func_exp(x, min):
    return 1-math.exp(1-(x/min))

for i in range(len(ID)):
    # guests_i = func_exp(GUESTS[i],GUESTS_min)
    # starts_i = func_exp(STARS[i],STARS_min)
    # income_i = func_exp(INCOME[i],INCOME_min)
    # list_restarunt[ID[i]] = guests_i+starts_i+income_i

    guests_i = (GUESTS[i]-GUESTS_min)/(GUESTS_max-GUESTS_min)
    starts_i = (STARS[i]-STARS_min)/(STARS_max-STARS_min)
    income_i = (INCOME[i]-INCOME_min)/(INCOME_max-INCOME_min)
    list_restarunt[ID[i]] = guests_i+starts_i+income_i
import operator
print(sorted(list_restarunt.items(), key=operator.itemgetter(1))[-3:])
