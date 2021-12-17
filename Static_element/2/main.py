

import numpy
from requests.api import post

# Упражнение 2.1

#X = [5, 6, 2, 5, 5, 4, 1, 1, 3, 5, 2, 4]
# X = [6,5,2,3,3,4,5,1,1]
# X = [5,4,6,2,2,5,4,2]
# X = [1, 3, 1, 1, 3, 6, 5, 5, 2, 4]
# print(len(X))
# X_mean  = numpy.mean(X)
# X_var = numpy.var(X)
# X_std = numpy.std(X)
# print("X = ", round(X_mean,3))
# print("S = ",round(X_var,3))
# print("S^2 = ",round(X_std,3))
# print(X_mean-X_std)
# print(X_mean+X_std)
# упражнение 2.2
import scipy.special
P = float(input("Вероятность: "))
n = int(input("Число первое:"))
k = int(input("Первый число интервала: "))
j = int(input("Второе число интервала: "))
SUM = 0
for i in range(k+1, j+1):
    C = scipy.special.binom(n, i)
    p = P**i
    q = (1-P)**(n-i)
    SUM += C*p*q
print(round(SUM, 3))
# Упражнение 2.3
# N = [3,6]
# E = [155,182,185,197]
# P_E = [[0.12,0.18,0.1,0.26],[0.02,0.05,0.04,0.23]]
# X_E = numpy.mean(E)
# S_E = numpy.var(E)
# X_sum = 0
# print(sum(P_E[1]))
# for  i in range(len(E)):
#     X_sum += (E[0]*(P_E[0][i]+P_E[1][i]))
# print(X_sum)
# X_sum = 0
# for i in range(len(N)):
#     X_sum += N[0]*sum(P_E[i])
# print(X_sum)
# print(X_E)
# print(S_E)
# list_N = [sum(P_E[0]),sum(P_E[1])]
#print(list_N[0]*(N[0]**2)+list_N[1]*(N[1]**2) -3.16**2 )

