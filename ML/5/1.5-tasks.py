import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial.distance import squareform, pdist
DATA = pd.read_csv("/home/hanmask/home/openedu/ML/5/tasks.csv",delimiter=',', index_col='Object')
coords = DATA.drop('Cluster', axis=1)
kmeans = KMeans(n_clusters=3, init=np.array([[11.0, 8.8], [13.0, 11.33], [10.25, 9.75]]), max_iter=100, n_init=1)
model = kmeans.fit(coords)
model.labels_.tolist()
alldistances = kmeans.fit_transform(coords)

coords[model.labels_==0]
#dir(alldistances)
#alldistances.i
dists = pdist(alldistances[model.labels_==0])
squareform(dists)
round(dists.mean(),3)
test = DATA[model.labels_==0]
round(np.mean(alldistances[model.labels_== 0]), 3)
list = []
for i in alldistances[model.labels_==0]:
    list.append( np.linalg.norm(i))
np.linalg.norm(alldistances[model.labels_==0])
round(np.mean(list),3)
