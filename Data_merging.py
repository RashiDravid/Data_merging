import pandas as pd

df = pd.read_csv("dwarf_stars.csv")

print(df.columns)
print(df.dtypes)
print(df.shape)

df = df.dropna()
print(df)

df["Radius"] = 0.102763*df["Radius"]

df1 = pd.read_csv("bright_stars.csv")

print(df1.columns)
print(df1.shape)

df1 = df.dropna()
print(df1)

df1["Radius"] = 0.102763*df1["Radius"]

import csv 

dwarf_stars = []
bright_stars = []

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dwarf_stars.append(row)

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        bright_stars.append(row)

headers_1 = dwarf_stars[0]
stars_data_1 = dwarf_stars[1:]

headers_2 = bright_stars[0]
stars_data_2 = bright_stars[1:]

headers = headers_1 + headers_2
stars_data = []

for index, data_row in enumerate(stars_data_2):
    stars_data.append(stars_data_1[index] + stars_data_2[index])


with open("stars.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)

df2 = pd.read_csv("stars.csv")
