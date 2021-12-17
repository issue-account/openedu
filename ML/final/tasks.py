import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

star = [0.802,0.876,0.689,0.228,0.802,0.609,0.743,0.981]
def liner_normirovka(x, x_min, x_max):
    y = (x-x_min)/(x_max-x_min)
    return y
x_predict = ["MIP","STDIP","EKIP","SIP","MC","STDC","EKC","SC"]
# avg mip = 78.241
# count = 202
DATA = pd.read_csv("/home/hanmask/home/openedu/ML/final/report.csv",
                   delimiter=',')
X_Predict = DATA.drop('TARGET', axis=1)
y = DATA["TARGET"]
for i in x_predict:
    x_min = min(X_Predict[i])
    x_max = max(X_Predict[i])
    X_Predict[i] = X_Predict[i].apply(lambda x: (x-x_min)/(x_max-x_min))
reg = LogisticRegression( random_state=2019, solver='lbfgs').fit(X_Predict, y.values.ravel())
round(reg.predict_proba([star])[:,1][0],3)
neigh = KNeighborsClassifier(n_neighbors=5, p=2)
neigh.fit(X_Predict, y)
neigh.predict_proba([star])
neigh.predict([star])
neigh.kneighbors([star])
round(1.15206451,3)
