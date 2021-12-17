import pandas as pd
import math

def X_t(x):
    return sum(x)/len(x)

def Q1(x,y):
    n = sum([(i-X_t(y))*(j-X_t(x)) for i,j in zip(y,x)])
    m = sum([(i-X)**2 for i in x])
    return n/m

def R2(x,y,Q1,Q0):
    m  = sum([(i-X_t(y))**2   for i   in y])
    t  = sum([(j-Q0-Q1*i)**2  for i,j in zip(x,y)])
    return 1-(t/m)

data = pd.read_csv("/home/hanmask/openedu/ML/2/test.csv")
X  = X_t(data.X)
Y  = X_t(data.Y)
Q_1 = Q1(data.X,data.Y)
Q_0 = Y-Q_1*X
R_2 = R2(data.X,data.Y,Q_1,Q_0)
print("X  =", X)
print("Y  =", Y)
print("Q1 =", round(Q_1,2))
print("Q0 =",round(Q_0,2))
print("R2 =",round(R_2,2))
