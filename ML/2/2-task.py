# import numpy as np
# from scipy import sparse
# x = np.array([[1,2,3],[4,5,6]])
# print("x:\n{}".format(x))
# eye = np.eye(4)
#
# sparse_matrix = sparse.csr_matrix(eye)
# print("\n Matrix in Scipy:\n{}".format(sparse_matrix))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = pd.read_csv("/home/hanmask/openedu/ML/2/candy-data.csv")
list_delete = ["Skittles wildberry", "Smarties candy"]
for i in list_delete:
    data.drop(data.index[(data["competitorname"] == i)],axis=0,inplace=True)

list_predictor = [i for i in data]
otclik = list_predictor[-2]
del list_predictor[0]
del list_predictor[-1]
del list_predictor[-2]
# print(data.chocolate.plot())
data.winpercent.plot()
