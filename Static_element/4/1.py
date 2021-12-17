
from statistics import NormalDist
from numpy.core.numeric import tensordot
import scipy.stats as st
import numpy as np
import pandas as pd
from os import stat
from typing import List
import numpy
from numpy.ma.core import left_shift, right_shift
import requests  # импортируем модуль
from scipy.stats import norm, poisson, chi2
send = requests.post(
    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Normal_172.csv")

list_U = [float(i) for i in send.text.split()]
alpha = 0.05
t = 1-alpha/2
X = numpy.mean(list_U)
S = numpy.var(list_U, ddof=1)
std = numpy.std(list_U,ddof=1)
print("X = ",X)
print("S = ",S)
print("S^2 = ",std)

n = len(list_U)
print("n = ", n)
# П
def U(a):
    t = st.t.ppf(1-0.05/2, df=len(a)-1)
    p = t*(sorted(a)[-1]-sorted(a)[0])
    q = numpy.sqrt(3*len(a))
    F_1 = 2*X - (p/q) - sorted(a)[len(a)-1]
    F_2 = 2*X + (p/q) - sorted(a)[0]
    print(F_1)
    print(round(F_2, 3))
    print(F_2 - F_1)
#U(list_u)

def P(X,n):
    t = st.t.ppf(1-0.05/2, df=len(a)-1)
    left = X - ((t*numpy.sqrt(X))/numpy.sqrt(n))
    right = X + t*numpy.sqrt(X)/numpy.sqrt(n)
    print(round(left, 2))
    print(round(right, 2))
    print(round(right*2, 2))
#P(X,n)

def B(a=1,X=1.0):
    q = X*(1-X/a)
    left = X/a - t*numpy.sqrt(q)/(numpy.sqrt(n)*a)
    right = X/a + t*numpy.sqrt(q)/(numpy.sqrt(n)*a)
    print(round(left, 2))
    print(round(right, 2))
    print(round(right*12))
#B(a=12,X=X)

def G(a,X):
    left = 1/X - (t*numpy.sqrt(1-1/X))/(numpy.sqrt(len(a)*X))
    right = 1/X + (t*numpy.sqrt(1-1/X))/(numpy.sqrt(len(a)*X))
    print(round(left, 2))
    print(round(right, 2))
    print(round(left*10))
#G(list_U,X)

def N(a=1, H=[]):
    X_sum = [pow(i-a, 2) for i in H]
    c1 = st.chi2.ppf(1-0.05/2, df=len(H))
    c2 = st.chi2.ppf(0.05/2, df=len(H))
    print(c1)
    print(c2)
    F_2 = sum(X_sum)/c2
    F_1 = sum(X_sum)/c1
    print("N interval")
    t = st.t.ppf(1-0.05/2, df=len(H)-1)
    min_x = X-t*S/np.sqrt(len(H))
    print("Q1 = ", round(F_1, 2))
    print("Q2 = ", round(F_2, 2))
    print("min =",round(min_x,2))
N(a=998,H=list_U)
#(list_U,X)
#B(a=12,X=X)