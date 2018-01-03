import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# import json


# result = pd.read_json("data/2017-11-26(2).json")
# result = pd.read_json("data2/2017(8).json")
result = pd.read_json("data3/target.json")
test = pd.read_json("data3/2016-01.json")


# f = open("data3/target.json", 'w').read()
# print(type(f))

result.head()
# print(type(result)

plt.close()

fig, axs = plt.subplots(2, 4, sharey=True)
# 溫度
result.plot(kind='scatter', x='Temperature',
            y='Precp', ax=axs[0][0], figsize=(16, 8))

# 相對濕度
result.plot(kind='scatter', x='RH', y='Precp', ax=axs[0][1])

# 海平面氣壓
result.plot(kind='scatter', x='SeaPres', y='Precp', ax=axs[0][2])

# 測站氣壓
result.plot(kind='scatter', x='StnPres', y='Precp', ax=axs[0][3])

# 露點溫度
result.plot(kind='scatter', x='Td dew point', y='Precp', ax=axs[1][0])

# 日曬時間
result.plot(kind='scatter', x='SunShine', y='Precp', ax=axs[1][1])

result.plot(kind='scatter', x='T Min', y='Precp', ax=axs[1][2])

result.plot(kind='scatter', x='T Max', y='Precp', ax=axs[1][3])

# plt.show()

feature_cols = ['Temperature', 'RH', 'SeaPres', 'StnPres',
                'Td dew point', 'T Max']

# std_dataset = {}
# tem = []
for key in feature_cols:
    count = 0
    for val in result[key]:
        val = (val - result[key].mean()) / result[key].std()
        result[key][count] = val
        count = count + 1
    print(result[key])


# feature_cols = ['SeaPres', 'PrecpMax10', 'StnPres']
X = result[feature_cols]
y = result.Precp
# X = std_dataset[feature_cols]
# y = std_dataset.Precp

lm = LinearRegression(normalize=True)
lm.fit(X, y)
print("Coefficient : ", lm.coef_)

# x_test = test[feature_cols]
# y_test = test.Precp
# plt.scatter(x_test, y_test, color='blue', marker='x')
# plt.plot(x_test, lm.predict(x_test), color='green')
# plt.xlabel('R')
# plt.ylabel('HR')
# plt.show()


# sc = StandardScaler()
# sc.fit(X)
# X_std = sc.transform(X)
# lm.fit(X_std, y)

# 印出截距
print(lm.intercept_)
print("RMSE : ", lm._residues)


r_squared = lm.score(X, y)
adj_r_squared = r_squared - (1 - r_squared) * \
    (X.shape[1] / (X.shape[0] - X.shape[1] - 1))

print("R^2:", r_squared)
print("adj_r_square:", adj_r_squared)

# print(result[feature_cols[1]])

# for i in range(7):
#     lm1 = LinearRegression()
#     lm1.fit(result[feature_cols[i]], y)
#     print(lm1.score(result[feature_cols[i]], y))


# print(lm.score(result['Temperature'], y))

# test_cols = ['Temperature', 'RH', 'SeaPres', 'StnPres',
#                 'Td dew point', 'SunShine', 'T Min', 'T Max']

# train = lm.predict(test[test_cols])
# print(train)
