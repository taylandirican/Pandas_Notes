import pandas as pd

data = pd.read_csv("datasets/Youtube.csv")


result = data.head(10)


result = data[5:].head()


result = data.columns
result_size = result.size


result = data.drop(
    [
        "thumbnail_link",
        "comments_disabled",
        "ratings_disabled",
        "video_error_or_removed",
        "description",
    ],
    axis=1,
    inplace=True,
)
result = data.columns


result = data[["likes", "dislikes"]].mean()


result = data[["likes", "dislikes", "title"]].head(50)


result = data[data["views"] == data["views"].max()][["title", "views"]]


result = data[data["views"] == data["views"].min()][["title", "views"]]


result = data[["views", "title"]].sort_values("views", ascending=False).head(10)


result = data.groupby("category_id")["likes"].mean().sort_values(ascending=False)


result = data.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)


result = data.groupby("category_id").size()


data["title_index"] = data["title"].str.len()


data["tag_count"] = data["tags"].apply(lambda x: len(x.split("|")))


def popular(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    tuples = list(zip(likesList, dislikesList))

    oranL = []

    for like, dislike in tuples:

        if (like + dislike) == 0:
            oranL.append(0)

        else:
            oranL.append(like / (like + dislike))

    return oranL


data["popular"] = popular(data)
result = data.sort_values("popular", ascending=False)[
    ["title", "likes", "dislikes", "popular"]
]


print(result)
