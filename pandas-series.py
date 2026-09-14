import pandas as pd
import numpy as np

# data
# numbers = [20, 30, 40, 50]
# letters = ["B", "T", 1, 23, 34, 5]
# scalar = [3]
# dict = {"a": 10, "b": 20, "c": 30, "d": 40}
# random_numbers = np.random.randint(10, 100, 6)
# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(3, [0, 1, 2, 3])
# pandas_series = pd.Series(
#     numbers, ["a", "b", "c", "d"]
# )  # ilk bölme values - ikinci bölme keys
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

# result = pandas_series["a"]
# result = pandas_series.iloc[0]  # Güncelleme yeni metot
# result = pandas_series.iloc[-1]
# result = pandas_series.iloc[2:]
# result = pandas_series.iloc[-2:]
# result = pandas_series["b"]
# result = pandas_series[["a", "c", "e"]]  # Hata verir
# result = pandas_series.reindex(["e"])   #verilerin indexlerini değiştirmek, düzenlemek ve benzetmek için vardır

# result = pandas_series.ndim  # boyut sayısı
# result = pandas_series.dtype  # type bilgisi
# result = pandas_series.shape  # boyut bilgisi
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series.mean()
# result = pandas_series + pandas_series
# result = np.sqrt(pandas_series)
# result = pandas_series >= 50
# result = pandas_series % 3 == 0


# print(pandas_series[result])
# print(result)


opel2018 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "grandland", "insignia"])

result = opel2018 + opel2019
print(result["astra"])
print(result["combo"])  # Hata
