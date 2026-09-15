import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

result = df
result = df.columns
result = df.head()  # İlk 5 satırı gösterir
result = df.head(10)  # İlk 10 satı
result = df.tail()  # Son 5 satır
result = df.tail(10)
result = df["Column1"].head()
result = df[["Column1", "Column2"]].head()
result = df[["Column1", "Column2"]].tail()
result = df[5:15][["Column1", "Column2"]].head()

result = df > 50
result = df[df > 50]
result = df[df % 2 == 0]
result = df[df["Column1"] % 2 == 1][["Column1", "Column2"]]
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1", "Column2"]]

result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1", "Column2"]]
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1", "Column2"]]


print(result)
