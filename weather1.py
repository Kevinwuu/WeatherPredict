import requests
from bs4 import BeautifulSoup
import json
import re


def read_data(month, day):
    url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017-'
    url = url + month + "-" + str(day)

    response = requests.get(url)

    # 一般python會自動編成big5，網頁的utf-8會變亂碼
    response.encoding = 'utf-8'

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
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
        # print(result[0])
        # 匹配完後會變成list
        title.append(result[0])
    print(title)

    # 抓取特定欄位下每筆資料
    rows = table.find_all('tr')

    # FOR
    # tem = []
    d = {}
    weather = {}
    sort = 1

    # 依序讀取每一欄天氣因素的所有資料,去除前兩個
    # 讀取每一行資料,去除最前面兩個奇怪字元
    for r in rows[2:]:
        # 每筆資料中間都隔了一個br,tem是[7]
        value = r.contents[7].string
        # print(value)

        # 去除字串尾部\xa0 空白字元
        # split不帶參數時為自動去除換行符...等
        # 存進字典中
        d[sort] = "".join(value.split())
        sort = sort + 1

        weather[title[3]] = d
    print("--------------------------------------------------------")
    # print("dictionary:\n", d, "\n")
    # json_str = json.dumps(d)
    # print("json data:\n", json_str)
    # weather[title[3]] = d
    print("Json:", json.dumps(weather, indent=4, sort_keys=True))
    # print("Json:", json.dumps(weather, indent=4))
