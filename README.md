
# 大數據分析期末報告

## 降雨量預測

### 作法
用BeautifulSoup()爬取網頁資料，拿過去的天氣資料與降雨量做training，透過regression求出回歸直線，再
用爬蟲抓取及時資料做testing，驗證準確率。

### 進度

craw_data : 爬取日報表資料。

#### 參考資料網站
[觀測資料查詢系統](http://e-service.cwb.gov.tw/HistoryDataQuery/)

[淡水測站日報表](http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017-12-05)

[淡水測站年報表](http://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017)

[即時降雨機率](https://weather.com/zh-TW/weather/hourbyhour/l/TWXX0021:1:TW)

