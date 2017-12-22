import requests
from bs4 import BeautifulSoup
import json
import re
import os


def rain():
    url = "https://weather.com/zh-TW/weather/hourbyhour/l/TWXX0021:1:TW"
    response = requests.get(url)

    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    # 讀取整張表格
    table = soup.find(id='twc-scrollabe').table.tbody

    # weather = {}
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

    # btn = soup.find(id='twc-scrollabe').find('div', 'ls-display-control').button
    for r in rows:
        # 找到降雨量欄位
        precip = r.find('td', 'precip').div.find('span', '').span.text
        # result = precip.select("div span")
        precip_result = precip.split('%')[0]
        # print(precip_result, '\n')
        rain.append(precip_result)
    return rain


def read_data(month, day):
    url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker='

    # 要讀取的日期
    date = "2017-" + month + "-" + str(day)
    url = url + date

    response = requests.get(url)

    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'

    # 解析HTML,lxml解析器速度較html.parser快
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())

    # 讀取表格
    table = soup.find(id='MyTable').tbody

    # 抓取所有標題
    titles = table.find('tr', 'second_tr').find_all('th')
    title = []
    for i in range(0, len(titles)):
        result = titles[i].text

        # 正則表達式去除括號內文字(替換成空)
        result = re.sub(r'\([^)]*\)', '', result)

        # 去除中文
        result = re.findall('[a-zA-Z]+', result)

        # 匹配完後會變成list
        title.append(result[0])
    # print(title)

    # 抓取特定欄位下每筆資料
    rows = table.find_all('tr')

    weather = {}

    # 依序讀取每一欄天氣因素的所有資料,去除前兩個
    for col in range(0, 15, 1):
        # 讀取每一行資料,去除最前面兩個奇怪字元
        # d = {}
        d = []
        # sort = 1
        for r in rows[2:]:
            # 每筆資料中間都隔了一個br,tem是[7]
            index = col * 2 + 1
            value = r.contents[index].string

            # 去除字串尾部\xa0 空白字元,split不帶參數時為自動去除換行符...等
            # 存進字典中
            # d[sort] = "".join(value.split())
            # sort = sort + 1
            value = "".join(value.split())
            d.append(value)
        # print(title[col])
        # print(d, "\n")
        weather[title[col]] = d
        # print("\n", weather[title[col]], "\n")
        # print("\n", weather, "\n")
    # print("--------------------------------------------------------")
    # print("weather:\n", weather, "\n")
    # print("Json:", json.dumps(weather, indent=4, sort_keys=True))
    r = rain()
    for i in range(8):
        r.append('0')
    weather['rain'] = r
    # 將json檔存在當前目錄下的data目錄
    file = date + ".json"
    dir = os.getcwd()
    path = dir + "\\data"
    # print(date, "已存到", path)
    if not os.path.isdir(path):
        os.mkdir(path)

    f = open(path + "\\" + file, 'w')
    f.write(json.dumps(weather, indent=4))
