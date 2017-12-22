import weather

# 設定從哪天開始往前爬取資料,日期時間都要是兩位數
today = 20
month = "12"

for i in range(today, (today - 1), -1):
    if i < 10:
        i = "0" + str(i)
        print(month, "/", i)
        weather.read_data(month, i)
    else:
        print(month, "/", i)
        weather.read_data(month, i)
