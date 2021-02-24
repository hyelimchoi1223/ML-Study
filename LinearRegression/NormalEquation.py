import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
train = pd.DataFrame(pd.read_csv(
    "ML-Study/LinearRegression/HousePrices/train.csv"), columns=["x0", "LotArea", "BedroomAbvGr", "YearBuilt", "SalePrice"])
train["YearBuilt"] = 2021-train["YearBuilt"]
train["x0"] = 1
#       x0  LotArea  BedroomAbvGr  YearBuilt  SalePrice
# 0      1     8450             3         18     208500
# 1      1     9600             3         45     181500
# 2      1    11250             3         20     223500
# 3      1     9550             3        106     140000
# 4      1    14260             4         21     250000
# ...   ..      ...           ...        ...        ...
# 1455   1     7917             3         22     175000
# 1456   1    13175             3         43     210000
# 1457   1     9042             4         80     266500
# 1458   1     9717             2         71     142125
# 1459   1     9937             3         56     147500
X = train[["x0", "LotArea", "BedroomAbvGr", "YearBuilt"]].values
# [[    1  8450     3    18]
#  [    1  9600     3    45]
#  [    1 11250     3    20]
#  ...
#  [    1  9042     4    80]
#  [    1  9717     2    71]
#  [    1  9937     3    56]]
Y = train[["SalePrice"]].values
# [[208500]
#  [181500]
#  [223500]
#  ...
#  [266500]
#  [142125]
#  [147500]]
theta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), Y)
print(theta)
# [[ 1.81257459e+05]
#  [ 1.87045321e+00]
#  [ 1.73028518e+04]
#  [-1.39959760e+03]]

# 테스트
test = pd.DataFrame(pd.read_csv(
    "ML-Study/LinearRegression/HousePrices/test.csv"), columns=["x0", "LotArea", "BedroomAbvGr", "YearBuilt", "SalePrice"])
train["YearBuilt"] = 2021-train["YearBuilt"]
train["x0"] = 1
