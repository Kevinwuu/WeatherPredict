import weather

# 設定從哪天開始
today = 20
month = "12"

# 往前連續爬取資料,日期時間格式都要是兩位數才行
for i in range(today, (today - 1), -1):
    if i < 10:
        i = "0" + str(i)
        print(month, "/", i)
        weather.get_data(month, i)
    else:
        print(month, "/", i)
        weather.get_data(month, i)
