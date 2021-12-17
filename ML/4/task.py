# import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
DATA = pd.read_csv("/home/hanmask/home/openedu/ML/4/task.csv",
                   delimiter=',', index_col='competitorname')
train_data = DATA.drop(['Boston Baked Beans', 'Dum Dums', 'Fruit Chews'])
X = pd.DataFrame(train_data.drop(['winpercent', 'Y'], axis=1))
y = pd.DataFrame(train_data['Y'])
reg = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())
test = pd.read_csv("/home/hanmask/home/openedu/ML/4/candy-test.csv",
                   delimiter=',', index_col='competitorname')
# AirHeads = test.loc['Tootsie Roll Midgies', :].to_frame().T
# reg.predict(AirHeads.drop(['Y'], axis=1))
test_data = pd.read_csv("/home/hanmask/home/openedu/ML/4/candy-test.csv", delimiter=',',
                        index_col='competitorname')
test_data
X_test = pd.DataFrame(test_data.drop(['Y'], axis=1))
Y_pred = reg.predict(X_test)
Y_pred_probs = reg.predict_proba(X_test)
Y_pred_probs.tolist()
Y_pred_probs_class_1 = Y_pred_probs[:,1]
Y_pred_probs_class_1.tolist()
round(Y_pred_probs_class_1[10], 3)
round(Y_pred_probs_class_1[6], 3)

Y_true = (test_data['Y'].to_frame().T).values.ravel()
Y_true
fpr, tpr, _ = metrics.roc_curve(Y_true, Y_pred)
round(metrics.roc_auc_score(Y_true, Y_pred_probs_class_1), 3)
metrics.recall_score(Y_true, Y_pred)
metrics.precision_score(Y_true, Y_pred)
