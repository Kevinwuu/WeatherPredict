import requests
from bs4 import BeautifulSoup
import json
import re
import os

url = "https://weather.com/zh-TW/weather/hourbyhour/l/TWXX0021:1:TW"
response = requests.get(url)

# 一般python會自動編成big5，網頁的utf-8會變亂碼
response.encoding = 'utf-8'

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# 讀取整張表格
table = soup.find(id='twc-scrollabe').table.tbody

weather = {}
rows = table.find_all('tr')
# print(rows)
# 找到所有兄弟節點來遍歷
map = soup.find('div', id='map').next_siblings
for m in map:
    name = m['class'][0]
    if name == 'todaymap__timestamp':
        date = m.text
        # print(m.text)

    # else:
        # print(m['class'], '\n')
        # print("none")
rain = []

btn = soup.find(id='twc-scrollabe').find('div', 'ls-display-control').button
# print(btn)
btn.click
for r in rows:
    # 找到降雨量欄位
    precip = r.find('td', 'precip').div.find('span', '').span.text
    # result = precip.select("div span")
    precip_result = precip.split('%')[0]
    # print(precip_result, '\n')
    rain.append(precip_result)



# 將json檔存在當前目錄下的data目錄
date1 = 'today'
file = date1 + ".json"
dir = os.getcwd()
path = dir + "\\data1"
# print(date1, "已存到", path)
if not os.path.isdir(path):
    os.mkdir(path)

# f = open(path + "\\" + file, 'w')
# f.write(json.dumps(rain, indent=4))
# print(json.dumps(rain, indent=4))
print(rain)

