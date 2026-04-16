import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("football_matches.csv")

# 勝敗判定
df["result"] = df.apply(
    lambda x: "home_win" if x["goal_home_ft"] > x["goal_away_ft"]
    else ("away_win" if x["goal_home_ft"] < x["goal_away_ft"] else "draw"),
    axis=1
)

# ホーム勝利
home_win = df[df["result"] == "home_win"]

# 英語グラフ
plt.hist(home_win["home_shots"], bins=20)
plt.title("Home Team Shots (Win)")
plt.xlabel("Shots")
plt.ylabel("Frequency")

# 保存
plt.savefig("shots_hist.png")

# 日本語グラフ
plt.hist(home_win["home_shots"], bins=20)
plt.title("ホーム勝利時のシュート数")
plt.xlabel("シュート数")
plt.ylabel("試合数")

# 保存
plt.savefig("shots_hist_JP.png")


plt.show()
