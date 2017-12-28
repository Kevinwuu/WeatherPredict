import day_data
import json


# for y in range(2016, 2017):
#     # 跑所有個月份
#     for m in range(1, 13):
#         if m < 10:
#             m = "0" + str(m)
#             # print(m)
#         day_data.get_data(y, m)
#         print(y, "/", m)


for y in range(2008, 2009):
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
        # print(data["ObsTime"])
        # print(path1)
        # 找到相同key的欄位合併資料
        for key, value in data.items():
            # 合併list

            data[key].extend(data1[key])


print(len(data["Precp"]))

# 把數值為T的去掉
count = 0
for p in data["Precp"]:
    if p == "T":
        data["Precp"][count] = 0.1
        # print(p)
    count = count + 1



# # 合併完所有年份資料後另存新檔
# addr = "data3/" + "target" + ".json"
# f = open(addr, 'w')
# f.write(json.dumps(data, indent=4, ensure_ascii=False))

