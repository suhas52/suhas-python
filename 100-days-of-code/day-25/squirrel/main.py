import pandas

squirrel_data = pandas.read_csv("squirrel_data.csv")

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


color_numbers = {
     "Gray": grey_squirrels_count,
     "Cinnamon": cinnamon_squirrels_count,
     "Black": black_squirrels_count,
}

df = pandas.DataFrame({
     "Colors" : list(color_numbers.keys()),
     "Numbers" : list(color_numbers.values())
})

df.to_csv("color_numbers.csv")