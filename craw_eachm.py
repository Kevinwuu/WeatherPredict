import weather1
import json
import os
# from os import work
# from os.work import  join

# 跑每年每個月份存成training 資料
# for m in range(1, 13):
#     if m < 10:
#         m = "0" + str(m)
#     for y in range(2008, 2018):
#         weather1.get_data(y, m)
#         print(y, "/", m)

# my_path = "data"
# for root, dirs, files in os.walk(my_path):
#     print(root)
#     print(dirs)
#     print(files)

# 資料目錄
my_path = "data"

for root, dirs, files in os.walk(my_path):
    dataset = {}
    Flag = 0
    if root != "data":
        # 依序跑資料夾
        for f in files:
            if f == "target.json":
                break
            full_path = os.path.join(root, f)
            print(full_path)
            json_data = open(full_path).read()
            data = json.loads(json_data)
            for key in data.keys():
                dataset.setdefault(key, []).extend(data[key])
            Flag = 1
        # 合併完整個資料夾再存檔
        if(Flag):
            f = open(root + "\\" + "target.json", 'w')
            f.write(json.dumps(dataset, indent=4, ensure_ascii=False))

# print(len(dataset["Precp"]))
# print(dataset["Precp"])
