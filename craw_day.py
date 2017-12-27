import day_data

# y = 2017
for y in range(2008, 2018):
    # 跑所有個月份
    for m in range(1, 13):
        if m < 10:
            m = "0" + str(m)
            day_data.get_data(y, m)
        day_data.get_data(y, m)
        print(m)
