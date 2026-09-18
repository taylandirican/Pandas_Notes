import pandas as pd

data = pd.read_csv("datasets/nba.csv")

result = data.head(10)


result = len(data)


result = data["player_height"].mean()


result = data["player_height"].max()


result = data[data["player_height"] == data["player_height"].max()]["player_name"]


result = data[(25 > data["age"]) & (data["age"] > 20)]
result = result[["team_abbreviation", "player_name", "age"]].sort_values(
    "age", ascending=False
)


result = data[data["player_name"].str.contains("John Holland")][
    ["team_abbreviation", "player_name"]
]


result = data.groupby("team_abbreviation")["player_height"].mean()


result = len(data.groupby("team_abbreviation"))


result = data.groupby("team_abbreviation")["player_name"].count()


data["index"] = data["player_name"].str.find("and")
result = data[data["index"] != -1]
print(result)
