import year_data

# 抓年度氣象局資料
year = 2017
for i in range(year, (year - 7), -1):
    year_data.get_data(i)
    print(i, "\n")
