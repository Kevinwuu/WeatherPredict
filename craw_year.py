import year_data
import json

# 抓年度氣象局天氣資料
# 設定起始日期
year = 2017

# 設定抓取多少年
num = 8
for i in range(year, (year - num), -1):
    year_data.get_data(i)
    print(i)

# 將起始日期json檔讀取當作基準
path = "data2/" + str(year) + ".json"
json_data = open(path).read()
data = json.loads(json_data)

# 讀取之前年份資料，依序合併其他年份資料
for j in range((year - 1), (year - num), -1):
    path = "data2/" + str(j) + ".json"
    json_data = open(path).read()

    # 讀成dict
    data1 = json.loads(json_data)
    # print(len(data.values()))

    # 找到相同key的欄位合併資料
    for key, value in data.items():
        # 合併list
        data[key].extend(data1[key])

count = 0
# 把數值為T的去掉
for p in data["Precp"]:
    if p == "T":
        data["Precp"][count] = 0.1
        # print(p)
    count = count + 1
# print(data)

# 合併完所有年份資料後另存新檔
addr = "data2/" + str(year) + "(" + str(num) + ")" + ".json"
f = open(addr, 'w')
f.write(json.dumps(data, indent=4, ensure_ascii=False))
