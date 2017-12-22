import rain_year

year = 2017
for i in range(year, (year - 7), -1):
    rain_year.read_data(i)
    print(i, "\n")
