
from os import sendfile
import requests #импортируем модуль
from  scipy.stats import poisson, norm
import numpy as np
from scipy.stats.stats import PearsonRConstantInputWarning
#send = requests.post(
#    'http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Normal_329.csv')
#send = requests.post(
#    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Binomial_282.csv")
#send = requests.post(
#    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Poisson_61.csv")
#send = requests.post(
#    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Uniform_150.csv")
#send = requests.post(
#    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Poisson_218.csv")
send = requests.post(
    "http://de.ifmo.ru/--openedu/appliedstatistics/course2019/ex2/Normal_314.csv")
list_U = [ float(i) for i in send.text.split()]  
# print(norm.fit(list_U))

D = np.var(list_U)
AVG = np.mean(list_U)
print(D)
print(round(AVG,2))
print(min(list_U))
print(max(list_U))
# answer = []
# list_set1 = sorted(set(list_U))
# #print(list_set1)
# for i in list_set1:
#     answer.append(poisson.pmf(list_U,i))
# print(round(np.mean(answer),2))
# print(poisson.fit(list_U))
# print(min(list_U))
# print("X = ", sum(list_U)/len(list_U))
# print("E = ", (max(list_U)+min(list_U))/2)
#делаем запрос
# file = open('report_2.csv,'w') #создаем файл для записи результатов
# file.write(send.text) #записываем результат
# file.close() #закрываем файл
