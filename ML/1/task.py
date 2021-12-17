import csv
import math
import pandas as pd
def mean(xs):
    '''Среднее значение числового ряда'''
    return sum(xs) / len(xs)
def median(xs):
    '''Медиана числового ряда'''
    n = len(xs)
    mid = n // 2
    if n % 2 == 1:
        return sorted(xs)[mid]
    else:
        return mean( sorted(xs)[mid-1:][:2] )
def variance(xs):
    '''Дисперсия (варианс) числового ряда,
       несмещенная дисперсия при n <= 30'''
    mu = mean(xs)
    n = len(xs)
    n = n-1 if n in range(1, 30) else n
    square_deviation = lambda x : (x - mu) ** 2
    return sum( map(square_deviation, xs) ) / n

file_csv = pd.read_csv("salary_and_population.csv")
list = ["Ставропольский край", "Пензенская область", "Кемеровская область", "Алтайский край", "Республика Мордовия"]
for i in list:
    file_csv.drop(file_csv.index[(file_csv["Region_RU"] == i)],axis=0,inplace=True)

salary = file_csv["AVG_Salary"]

print("Выборочное Среднее: ",round(sum(salary)/len(salary),2))
print("Медиана: ",round(median(salary),2))
print("Дисперсия: ",round(variance(salary),2))
print("Отклонение: ",round(math.sqrt(variance(salary)),2))
