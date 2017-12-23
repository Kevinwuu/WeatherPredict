import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# import json

result = pd.read_json("data/2017-11-26(2).json")


# print(data)
# result.head()
# print(result)


plt.close()
fig, axs = plt.subplots(1, 5, sharey=True)
result.plot(kind='scatter', x='Temperature', y='Precp', ax=axs[0], figsize=(16, 8))
result.plot(kind='scatter', x='RH', y='Precp', ax=axs[1])
result.plot(kind='scatter', x='SeaPres', y='Precp', ax=axs[2])
result.plot(kind='scatter', x='StnPres', y='Precp', ax=axs[3])
result.plot(kind='scatter', x='Td', y='Precp', ax=axs[4])
plt.show()
