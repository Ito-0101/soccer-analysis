import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("football_matches.csv")

df["result"] = df.apply(
    lambda x: "home_win" if x["home_goals"] > x["away_goals"]
    else ("away_win" if x["home_goals"] < x["away_goals"] else "draw"),
    axis=1
)

home_win = df[df["result"] == "home_win"]

plt.hist(home_win["home_shots"], bins=20)
plt.title("Home Team Shots (Win)")
plt.xlabel("Shots")
plt.ylabel("Frequency")
plt.show()
