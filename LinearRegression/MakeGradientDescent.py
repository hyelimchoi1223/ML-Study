import pandas as pd
import matplotlib.pyplot as plt
train = pd.DataFrame(pd.read_csv("D:\\1.Personal\\Github\\ML-Study\\LinearRegression\\HousePrices\\train.csv"))

fig, ax = plt.subplots(1, 3, figsize=(9,3), sharey=True)
ax[0].scatter(train["LotArea"].astype(int), train["SalePrice"].astype(int))
ax[0].grid()
ax[0].set(xlabel='Area', ylabel='Price')

ax[1].scatter(train["YearBuilt"].astype(int), train["SalePrice"].astype(int))
ax[1].grid()
ax[1].set(xlabel='YearBuilt', ylabel='Price')

ax[2].scatter(train["YearRemodAdd"].astype(int), train["SalePrice"].astype(int))
ax[2].grid()
ax[2].set(xlabel='YearRemodAdd', ylabel='Price')
plt.show()
