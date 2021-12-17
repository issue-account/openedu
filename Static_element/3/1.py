from typing import List
import seaborn as sns
import numpy as np
import pandas as pd
from pandas.core.indexes.base import Index
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial.distance import squareform, pdist
N = 10
data = pd.read_csv("/home/hanmask/home/openedu/Static_element/3/report.csv",
                   delimiter=',')
#list_delete=["Altai Republic","Magadan Region"]
#list_delete = ["Магаданская обл.", "г. Санкт-Петербург","Тульская область"]
#list_delete = ["Орловская область", "Нижегородская область", "Новосибирская область"]
#list_delete = ["Республика Татарстан", "Республика Марий Эл"]
#list_delete = ["Магаданская обл.", "г. Санкт-Петербург", "Тульская область"]
#list_delete = ["Республика Алтай","Магаданская обл."]
#list_delete = ["Рязанская область", "Свердловская область", "Чеченская Республика", "Ростовская область"]
#list_delete = ["Рязанская область", "Свердловская область", "Чеченская Республика", "Ростовская область"]
#list_delete = ["Смоленская область", "Чувашская Республика", "Костромская область", "Саратовская область"]
list_delete = ["Орловская область", "Нижегородская область", "Новосибирская область"]
for i in list_delete:
    data.drop(data.index[(data["REGION_NAME"] == i)], axis=0, inplace=True)
COUNT = len(data.index)
AVG = data["SALARY"].mean()
print(f"AVG = {round(AVG,2)}")
MEDIAN = data["SALARY"].median()
print(f"MEDIAN = {MEDIAN}")
VARIANCE = data["SALARY"].var(ddof=0)
print("Variance_1 = ",round(VARIANCE, 2))
VARIANCE = data["SALARY"].var()
print("Variance_2 = ",round(VARIANCE,2))
#print(round(data["SALARY"].std(), 2))
#print(VARIANCE
LIST_X = data["SALARY"].to_list()
s = pd.Series(LIST_X)
l = (max(LIST_X)-min(LIST_X))/N
bins = list(range(min(LIST_X), max(LIST_X)+int(l), int(l)))
res = s.groupby(pd.cut(s, bins=bins, right=False)).size()
for i in range(10):
    print(f"{i+1}",res.to_list()[i])
answer_list = [21,33,53]
LIST_X_sort =sorted((LIST_X))
for i in answer_list:
    print(LIST_X_sort[i-1])
