import weather
import json

# 設定從哪天開始
today = 30
month = "11"

# 爬取幾天資料
num = 30

# 往前連續爬取資料,日期時間格式都要是兩位數才行
for i in range(today, (today - num), -1):
    if i < 0:
        print("error !")
        break
    if 0 <= i < 10:
        i = "0" + str(i)
    print(month, "/", i)
    weather.get_data(month, i)


def dmerge():
        # 將起始日期json檔讀取當作基準
    path = "data/" + "2017" + "-" + month + "-" + str(today) + ".json"
    json_data = open(path).read()
    data = json.loads(json_data)
    # print(data)

    # 讀取之前資料，依序合併其他年份資料
    for j in range((today - 1), (today - num), -1):
        path1 = "data/" + "2017" + "-" + month + "-" + str(i) + ".json"
        json_data1 = open(path1).read()
        data1 = json.loads(json_data1)
        # print(len(data.values()))

        # 找到相同key的欄位合併list資料
        for key, value in data.items():
            data[key].extend(data1[key])
    # print(data["Precp"][1])
    count = 0
    # r = [p:for p in data["Precp"]]

    # 把數值為T的去掉
    for p in data["Precp"]:
        if p == "T":
            data["Precp"][count] = 0.1
            # print(p)
        count = count + 1
    # print(data["Precp"])

    # 合併完所有年份資料後另存新檔
    addr = "data/" + "2017" + "-" + month + "-" + \
        str(today) + "(" + str(num) + ")" + ".json"
    f = open(addr, 'w')
    f.write(json.dumps(data, indent=4, ensure_ascii=False))


dmerge()
