import pandas as pd

data = pd.read_csv("İmdb.csv")

# Veri hakkında bilgi
result = data
result = data.columns
result = data.info()

# Kayıtlar
result = data.head()
result = data.head(10)
result = data.tail()
result = data.tail(10)

# Kolon Seçme
result = data["Movie Name"]
result = data["Movie Name"].head()
result = data[["Movie Name", "Movie Rating"]].head()
result = data[["Movie Name", "Movie Rating"]].tail(7)
result = data[5:][["Movie Name", "Movie Rating"]].head()

# Karşılaştırma
result = data["Movie Rating"] >= 8.0
result = data[result][["Movie Name", "Movie Rating"]].head(50)


print(result)
