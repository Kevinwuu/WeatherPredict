import requests
from bs4 import BeautifulSoup
import json
import re
import os


# 抓降雨因素資料
def get_data(year, month):
    url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/MonthDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker='

    # 要讀取的日期

    url = url + str(year) + "-" + str(month)

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

        # 去除中文，匹配英文跟數字以及所有空白
        result = re.findall('[a-zA-Z0-9\s]+', result)

        # 解決例外狀況
        if result[0] == "10" or result[0] == "A":
            result = [result[1]]

        # 匹配完後會變成list,用index取值後刪除字串結尾空白
        title.append(result[0].rstrip())
    # print(title)

    # 抓取特定欄位下每筆資料
    rows = table.find_all('tr')

    weather = {}

    # 依序讀取每一欄天氣因素的所有資料,共31種
    for col in range(0, 32, 1):
        # 讀取每一行資料,去除最前面兩個奇怪字元

        # 創建暫存list，存取每項資料的所有數值
        d = []
        # sort = 1

        # 讀取每一行，從最上面標題行之後開始
        for r in rows[2:]:

            # 每欄資料中間都隔了一個br,tem是[7]
            index = col * 2 + 1
            value = r.contents[index].string

            # 去除字串尾部\xa0 空白字元,split不帶參數時為自動去除換行符...等
            # 存進字典中

            value = "".join(value.split())
            d.append(value)

        weather[title[col]] = d

    # print("Json:", json.dumps(weather, indent=4, sort_keys=True))

    # 將json檔存在當前目錄下的data3目錄
    # if 0 < month < 10:
    #     file = "0" + str(month) + ".json"
    file = str(month) + ".json"

    dir = os.getcwd()
    path = dir + "\\data3"
    # print(date, "已存到", path)

    # 創建資料夾
    if not os.path.isdir(path):
        os.mkdir(path)

    f = open(path + "\\" + str(year) + "-" + file, 'w')
    f.write(json.dumps(weather, indent=4))


