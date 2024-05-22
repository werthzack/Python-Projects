import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240522.csv")
primary_fur_data: pandas.Series = squirrel_data["Primary Fur Color"]

primary_colors = list(primary_fur_data.unique())

fur_color_data = []
fur_count_data = []
for color in primary_colors:
    if type(color) is not str:
        continue
    fur_color_data.append(color)
    fur_count = len(squirrel_data[primary_fur_data == color])
    fur_count_data.append(fur_count)

new_fur_data = {
    "Fur_Color": fur_color_data,
    "Count": fur_count_data
}
new_fur_dataframe = pandas.DataFrame(new_fur_data)
new_fur_dataframe.to_csv("./Fur_Data.csv")
