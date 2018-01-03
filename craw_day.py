import day_data
import json

# 爬training 資料
# for y in range(2016, 2017):
#     # 跑所有個月份
#     for m in range(1, 13):
#         if m < 10:
#             m = "0" + str(m)
#             # print(m)
#         day_data.get_data(y, m)
#         print(y, "/", m)

# 放置最終合併資料
dataset = {}
for y in range(2008, 2016):
    # 將每年一月的json檔讀取當作基準
    path = "data3/" + str(y) + "-01" + ".json"
    json_data = open(path).read()
    data = json.loads(json_data)
    # print(data["ObsTime"])

    # 依序將當年其他月份資料合併
    for m in range(2, 13):
        # 可改寫法
        if m < 10:
            m = "0" + str(m)

        path1 = "data3/" + str(y) + "-" + str(m) + ".json"
        json_data1 = open(path1).read()
        # 讀成dict
        data1 = json.loads(json_data1)

        # 找到相同key的欄位合併資料
        for key in data.keys():
            # 合併list
            data[key].extend(data1[key])
    for key in data.keys():
        dataset.setdefault(key, []).extend(data[key])
print(len(dataset["Precp"]))


# 將數值T改為0.1,數值X改為0
for v in dataset.values():
    num = v.count('T')
    while (num > 0):
        i = v.index('T')
        v[i] = '0.1'
        num = num - 1

    num1 = v.count('X')
    while (num1 > 0):
        i = v.index('X')
        v[i] = '0'
        num1 = num1 - 1
    num2 = v.count('')
    while (num2 > 0):
        i = v.index('')
        v[i] = '0'
        num2 = num2 - 1

# print(dataset.keys())
# print(len(dataset["Precp"]))

# 合併完所有年份資料後另存新檔
addr = "data3/" + "target" + ".json"
f = open(addr, 'w')
f.write(json.dumps(dataset, indent=4, ensure_ascii=False))
