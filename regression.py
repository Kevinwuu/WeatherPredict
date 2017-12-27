import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# import json

# result = pd.read_json("data/2017-11-26(2).json")
result = pd.read_json("data2/2017(8).json")


result.head()
# print(result)

plt.close()

fig, axs = plt.subplots(2, 4, sharey=True)
result.plot(kind='scatter', x='Temperature', y='Precp', ax=axs[0][0], figsize=(16, 8))
result.plot(kind='scatter', x='RH', y='Precp', ax=axs[0][1])
result.plot(kind='scatter', x='SeaPres', y='Precp', ax=axs[0][2])
result.plot(kind='scatter', x='StnPres', y='Precp', ax=axs[0][3])
result.plot(kind='scatter', x='Td dew point', y='Precp', ax=axs[1][0])
result.plot(kind='scatter', x='SunShine', y='Precp', ax=axs[1][1])
result.plot(kind='scatter', x='T Min', y='Precp', ax=axs[1][2])
result.plot(kind='scatter', x='T Max', y='Precp', ax=axs[1][3])

plt.show()

feature_cols = ['Temperature', 'RH', 'SeaPres', 'StnPres', 'Td dew point', 'SunShine', 'T Min', 'T Max']
X = result[feature_cols]
y = result.Precp
lm = LinearRegression()
lm.fit(X, y)
print("Coefficient : ", lm.coef_)
print("RMSE : ", lm._residues)
