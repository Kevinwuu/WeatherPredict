import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
import json

json_data = open("data2/2017.json").read()

json_data1 = open("data2/2016.json").read()


data = json.loads(json_data)
data1 = json.loads(json_data1)
for key in data:
    for key1 in data1:
        if key == key1:
            for i in range(len(data1[key1])):
                data[key].append(data1[key1][i])
    # print(data[key1])
    # data[key].append(data1[key1])


# print(data)
f = open("data2/target.json", 'w')
f.write(json.dumps(data, indent=4, ensure_ascii=False))
result = pd.read_json("data2/target.json")
# reg = pd.read_json("data2/2017.json")
# for i in range(7):
#     data = pd.read_json("data2/2017.json")

# data = json.dump(open("data2/2017.json"), [json.load(open('data2/2016.json')), json.load(open('data2/2015.json')), json.load(open('data2/2014.json'))])

# today = pd.read_json("data1/today.json")
# res = pd.merge(data, today)
# data1 = json.loads('data/2017-12-05.json')
# f = open("data/2017-12-04.json", 'w')
# data1 = json.loads('f')
# print(data)
# data.head()
# print(data)


plt.close()
fig, axs = plt.subplots(1, 2, sharey=True)
result.plot(kind='scatter', x='氣溫Temperature', y='降水量Precp', ax=axs[0], figsize=(16, 8))
# data.plot(kind='scatter', x='RH', y='rain', ax=axs[1])
# data.plot(kind='scatter', x='WSGust', y='rain', ax=axs[2])
# data.plot(kind='scatter', x='Temperature', y='rain', ax=axs[3])
plt.show()
