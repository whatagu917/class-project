import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
pd.set_option("display.unicode.east_asian_width", True)

# csvファイルをデータフレームに読み込む
df = pd.read_csv("download_2/pop_eta.csv", index_col="全国・都道府県", encoding="utf-8")

# 2023年と2022年の列データで，人口の増減を棒グラフで表示する
# 
df = df.drop("全国", axis=0) # 全国のデータを除外

df["2023年"] = pd.to_numeric(df["2023年"].str.replace(",", ""))
df["2020年"] = pd.to_numeric(df["2020年"].str.replace(",", ""))

df["増減倍率"] = (df["2023年"] - df["2020年"]) / df["2020年"]
df = df.sort_values("増減倍率", ascending=False)

# 増減倍率を棒グラフで表示
df["増減倍率"].plot.bar(figsize=(10, 6))
plt.show()
