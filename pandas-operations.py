import pandas as pd
import numpy as np

data = {
    "Column1": [1, 2, 3, 4, 5],
    "Column2": [10, 20, 13, 20, 58],
    "Column3": ["abc", "bac", "adee", "ba", "dea"],
}

df = pd.DataFrame(data)


def kareal(x):
    return x * x


kareal2 = lambda x: x * x


result = df
result = df["Column2"].unique()  # Tekrarlayan verileri bire indirir
result = df["Column2"].nunique()  # Tekrar olmadan oluşan dizinin adedini verir
result = df["Column2"].value_counts()  # Veri sayılarını verir
result = df["Column1"] * 2
result = df["Column1"].apply(
    kareal
)  # Belirtilen fonksiyona parametre olarak dfdeki verileri atar, fonk parametreli yazılmaz () konulmaz
result = df["Column2"].apply(kareal2)
result = df["Column2"].apply(lambda x: x * x)
result = df["Column3"].apply(len)  # Verinin karakter sayısını belirtir
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info()
result = df.sort_values("Column2")
result = df.sort_values("Column3")
result = df.sort_values("Column2", ascending=False)  # Ters sıralar

customersA = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Taylan", "B", "Ali", "Canan"],
    "LastName": ["Dirican", "A", "Çelik", "Toprak"],
}

data = pd.DataFrame(customersA)
data = data.pivot_table(
    index="CustomerId", columns="LastName", values="FirstName", aggfunc="first"
)  # values str olamaz ama aggfunc first olursa str olabilir


print(data)
print(result)
