import pandas as pd

data = pd.read_csv("nba.csv")

data.dropna(inplace=True)  # inplace: Data üzerinde gerçekleşir
data.drop("index", axis=1, inplace=True)

# print(data.columns)

# data["player_name"] = data["player_name"].str.upper()
# data["player_name"] = data["player_name"].str.lower()
# data["index"] = data["player_name"].str.find("a")

# data = data[data.player_name.str.contains("George")]
# data = data.college.str.replace(" ", "-")

data[["First_Name", "Last_Name"]] = (
    data["player_name"]
    .loc[data["player_name"].str.split().str.len() == 2]
    .str.split(expand=True)
)


print(data.head(10))
