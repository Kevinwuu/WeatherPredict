
# 降雨量預測
:computer:

## 作法
用BeautifulSoup()爬取網頁資料，拿過去的天氣資料與降雨量做training，透過regression求出回歸直線，再
用爬蟲抓取及時資料做testing，驗證準確率。

## 下雨定義
	1.大雨(heavy rain)：
		指24小時累積雨量達80毫米以上，或時雨量達40毫米以上之降雨現象。
	2.豪雨(extremely heavy rain)：
		指24小時累積雨量達200毫米以上，或3小時累積雨量達100毫米以上之降雨現象。
		若24小時累積雨量達350毫米以上稱之為大豪雨(torrential rain)。
		24小時累積雨量達500毫米以上稱之為超大豪雨(extremely torrential rain)。

## 使用工具
Python 3.5.3

BeautifulSoup

pandas

sklearn.linear_model

...

## 檔案
craw_data : 爬取日報表資料。

craw_rain : 爬取即時降雨機率。

craw_year : 爬取年報表資料。

regression : 讀取資料畫出相關性，求regression方程式。

## 進度



## 待辦
- [x] dict讀進json中文亂碼，但在python下可正常顯示。

- [ ] 如何自動點擊，顯示隱藏的html

- [ ] 年報表資料key值尚未去中文

- [ ] 將日報表資料作合併。

- [ ] regression到底有沒有相關性@@



### 參考資料網站
[觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/)

[淡水測站日報表](http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017-12-05)

[淡水測站年報表](http://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017)

[即時降雨機率](https://weather.com/zh-TW/weather/hourbyhour/l/TWXX0021:1:TW)

[台灣氣象站位置分布圖](http://www.cwb.gov.tw/V7/google/gmap.php?id=46690)

[下雨定義與降雨機率](http://www.metapp.org.tw/index.php/weatherknowledge/39-rainfall/56-2008-12-25-08-45-32)

