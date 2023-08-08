print("start csv read")

import pandas
df = pandas.read_csv('pokemon.csv')
print(df["Name"])

#for loop --> for each row you execute code

for r,rij in df.iterrrows():
    print(r)
    print("Huidige naam is " + rij["Name"])