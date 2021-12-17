import statistics as std
from numpy.ma.core import sqrt
import statsmodels.stats.diagnostic as stsd
from os import altsep, scandir
from pandas.core.base import DataError
import scipy.stats  as st
import numpy as np
import pandas as pd
import scipy
import requests

send = requests.post(
    "https://courses.openedu.ru/assets/courseware/v1/43aa2362f6abd9d0f341452b862304ab/asset-v1:ITMOUniversity+ELSTATAN+fall_2021_ITMO+type@asset+block/itog_sample_5.csv")

DATA= [float(i) for i in send.text.split()]
N=10
X = np.mean(DATA)
print("X = ",round(X,3))
print("1/X = ",round(1/X,3))

S = np.var(DATA,ddof=1)
std = np.std(DATA,ddof=1)
print("S = ",round(S,3))
s = pd.Series(DATA)
l = (max(DATA)-min(DATA))/N
bins = [0,]
k = min(DATA)
for i in range(11):
    bins.append(k)
    k = k+l
print("//////////////////")
res = s.groupby(pd.cut(s, bins=bins, right=False)).size()
print(res)
t = [3,6,9]
for i in t:
    print(f"{i} = ",res.to_list()[i-1])
t = 1-0.05/2
p = t*(max(DATA)-min(DATA))
q = np.sqrt(3*len(DATA))
F = 2*X -(p/q) - max(DATA)
print(round(F,3))
n_len = len(DATA)
Q_1 = DATA[1]
Q_2 = DATA[-1]
f_1 = 2*X - (t*(Q_2-Q_1))/np.sqrt(3*n_len) - Q_2
f_2 = 2*X + (t*(Q_2-Q_1))/np.sqrt(3*n_len) - Q_1
print(round(f_1, 3))
print(round(f_2, 3))

def U(a):
    t = st.t.ppf(1-0.05/2, df=len(a)-1)
    p = t*(sorted(DATA)[-1]-sorted(DATA)[0])
    q = np.sqrt(3*len(DATA))
    F_1 = 2*X - (p/q) - sorted(DATA)[len(DATA)-1]
    F_2  =2*X + (p/q) - sorted(DATA)[0]
    print("U распределние")
    print("Q1 = ",round(F_1,3))
    print("Q2 = ",round(F_2,3))
    print("///////////////")

def E(a):
    t = st.t.ppf(1-0.05/2, df=len(a)-1)
    F_1 = (1/X)-(t/(np.sqrt(len(a))*X))
    F_2 = (1/X)+(t/(np.sqrt(len(a))*X))
    print(round(F_1,3))
    print(round(F_2,3))
def N(a):
    t = st.t.ppf(1-0.05/2, df=len(a)-1)
    X = np.mean(a)
    F_1 =X- (t*np.std(a,ddof=1))/np.sqrt(len(a))
    c2 = st.chi2.ppf(0.05/2, df=len(a)-1)
    X_sum = [pow(i-X, 2) for i in a]
    F_2 = sum(X_sum)/c2
    print("N распределние")
    print("min x = ", round(min(DATA), 3))
    print("max x = ", round(max(DATA), 3))
    print("Q1 = ",round(F_1,3))
    print("Q2 = ",round(F_2, 3))
    print("////////")
#N(DATA)
def p(a):
    return abs(np.sqrt(len(DATA))*((X-a)/S))


import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF
from statsmodels.sandbox.stats.multicomp import multipletests
from collections import Counter
from tqdm import tqdm_notebook


def apply_kstest():
    print(np.sqrt(len(DATA)*S))
    c2 = st.chi2.ppf(1-0.05/2, df=len(DATA)-1)
    print(c2)
    t = st.t.ppf(1-0.05/2, df=len(DATA)-1)
    d = []
    for i in res.to_list():
        d.append(i/len(DATA))
    print(d)
    print(max(d)*np.sqrt(len(DATA)))
    print(sps.kstest(d,"uniform"))
    # ecdf = ECDF(sample)


apply_kstest()
