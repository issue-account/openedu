import numpy as np
import math
import requests

send = requests.post(
    "https://courses.openedu.ru/assets/courseware/v1/1bc10f8718ccadc8421f5086055dbbb2/asset-v1:ITMOUniversity+ELSTATAN+fall_2021_ITMO+type@asset+block/Hypothesis_1_16.csv")
data = [float(i) for i in send.text.split()]
n = len(data)
X = np.mean(data)
S = np.std(data,ddof=1)
print("X = ",round(X, 3))
print("S = ",round(S, 3))
def p(a):
    return abs(math.sqrt(len(data))*((X-a)/S))
print("p(X) = ",round(p(105), 3))
