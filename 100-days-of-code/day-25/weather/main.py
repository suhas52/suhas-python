import pandas

data = pandas.read_csv("weather_data.csv")

# temp_list = data["temp"].to_list()
# average = data.temp.mean()
maximum = data.temp.max()
# print(average)
# print(maximum)

monday = data[data.day == "Monday"]
print((monday.temp * 1.8) + 32)