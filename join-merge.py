import pandas as pd

# customers = {
#     "CustomerId": [1, 2, 3, 4],
#     "FirstName": ["Taylan", "B", "Ali", "Canan"],
#     "LastName": ["Dirican", "A", "Çelik", "Toprak"],
# }

# orders = {
#     "OrderTd": [10, 11, 12, 13],
#     "CustomerId": [1, 2, 5, 7],
#     "OrderDate": ["2010-07-04", "2010-07-04", "2010-07-07", "2012-07-04"],
# }

# df_customers = pd.DataFrame(customers)
# df_orders = pd.DataFrame(orders)


# result = pd.merge(df_customers, df_orders, how="inner")
# result = pd.merge(df_customers, df_orders, how="left")
# result = pd.merge(df_customers, df_orders, how="right")


# print(df_customers)
# print(df_orders)


customersA = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Taylan", "B", "Ali", "Canan"],
    "LastName": ["Dirican", "A", "Çelik", "Toprak"],
}


customersB = {
    "CustomerId": [4, 5, 6, 7],
    "FirstName": ["Yağmur", "Çınar", "Cengiz", "Can"],
    "LastName": ["Bilge", "Yılmaz", "Yılmaz", "Turan"],
}


df_customersA = pd.DataFrame(customersA)
df_customersB = pd.DataFrame(customersB)

result = pd.concat([df_customersA, df_customersB])
result = pd.concat([df_customersA, df_customersB], axis=1)
result = pd.merge(df_customersA, df_customersB, how="outer")


print(result)
