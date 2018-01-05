import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

# import json


# result = pd.read_json("all_data/2008-01.json")
# result = pd.read_json("data2/2017(8).json")
result = pd.read_json("data/08/target.json")
test = pd.read_json("all_data/2017-01.json")


result.head()
# print(result)

plt.close()

fig, axs = plt.subplots(2, 3, sharey=True)
# 溫度
result.plot(kind='scatter', x='Temperature',
            y='Precp', ax=axs[0][0], figsize=(16, 8))

# 相對濕度
result.plot(kind='scatter', x='RH', y='Precp', ax=axs[0][1])

# 海平面氣壓
result.plot(kind='scatter', x='SeaPres', y='Precp', ax=axs[0][2])


# 露點溫度
result.plot(kind='scatter', x='WS', y='Precp', ax=axs[1][0])

# 日曬時間
result.plot(kind='scatter', x='SunShine', y='Precp', ax=axs[1][1])

plt.show()

feature_cols = ['Temperature', 'RH', 'SeaPres',
                'WS', 'SunShine']


x_train = result[feature_cols]
y_train = result.Precp
x_test = test[feature_cols]

lm = LinearRegression(normalize=True)

# 標準化
sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

# lm.fit(X_std, y)
lm.fit(x_train, y_train)

# # 主成分分析PCA
# pca = PCA(n_components=2)
# x_train_pca = pca.fit_transform(x_train_std)
# x_test_pca = pca.transform(x_test_std)

# lab_enc = preprocessing.LabelEncoder()
# trainingScores = y_train
# encoded = lab_enc.fit_transform(trainingScores)

# # 邏輯斯蒂迴歸預測
# lr = LogisticRegression(random_state=1)
# lr.fit(x_train_pca, y_train)
# y_pred = lr.predict(x_test_pca)

print("Coefficient : ", lm.coef_)



# 誤差值
# r_squared = lm.score(X, y)
# adj_r_squared = r_squared - (1 - r_squared) * \
#     (X.shape[1] / (X.shape[0] - X.shape[1] - 1))

# 印出截距
print("Intercept:", lm.intercept_)
print("RMSE : ", lm._residues)
# print("R^2:", r_squared)
# print("adj_r_square:", adj_r_squared)

# pipe_lr = Pipeline([('sc', StandardScaler()), ('pca', PCA(n_components=2)), ('lr', LogisticRegression(random_state=1))])
# pipe_lr.fit(X_train, y_train)
# pipe_lr.score(X_test, y_test)

a = result[result.Precp == 0.0].index.tolist()
# print(result["Precp"].index('0'))
print(len(a))

