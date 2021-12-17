import csv

Y, EMA_list, number, test = [], [], [int(input("Введите первое значение ряда: ")), int(
    input("Введите второе значение ряда: "))], 0


def EMA(y, a, s):
    return a*y+((1-a)*s)


with open('task3-2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if test != 0:
            Y.append(float(row[0]))
        else:
            test = 1

# 2.1, 2.2 tasks
test, s = 0, 0
a = float(input("Введите коэффициент: "))
for i in range(len(Y)):
    if test == 0:
        s = EMA(Y[i], a, s)
    else:
        test = 1
        s = EMA(Y[i], a, s)
    EMA_list.append(s)

print(f"y({number[0]}) =", round(EMA_list[number[0]-1], 2))
print(f"y({number[1]}) =", round(EMA_list[number[1]-1], 2))

# 2.3, 2.4, 2.5 tasks


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


def X_t(x):
    return sum(x)/len(x)


def R2(x, y, Q1, Q0):
    m = sum([(i-X_t(y))**2 for i in y])
    t = sum([(j-Q0-Q1*i)**2 for i, j in zip(x, y)])
    return 1-(t/m)


a, b = linreg(range(len(Y)), Y)  # your x,y are switched from standard notation
#answer on 2.3 task
print("a =",  round(a, 2))
#answer on 2.4 task
print("Yx = ", round(a*100+b))
R_2 = R2(range(len(Y)), Y, a, b)
print("R2 = ", round(R_2, 2))
