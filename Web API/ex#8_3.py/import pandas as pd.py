import pandas as pd
import matplotlib.pyplot as plt

# データを読み込む
df = pd.read_csv("download_2/pop_eta.csv", index_col="全国・都道府県", encoding="utf-8")

# 列名を標準化
df.columns = df.columns.str.replace(" ", "").str.replace("年", "")
print(df.columns)  # 変更後の列名を確認

# 全国データを除外
df = df.drop("全国", axis=0)

# 必要な列を数値に変換
years = ["2005", "2010", "2015", "2020", "2023"]  # 年代に対応する列名を修正
for year in years:
    if year in df.columns:  # 列名が存在する場合のみ実行
        df[year] = pd.to_numeric(df[year].str.replace(",", ""), errors="coerce")
    else:
        print(f"列 '{year}' が存在しません。列名を確認してください。")

# 出身都道府県を指定
home_prefecture = "東京都"  # 出身都道府県名に置き換える
if home_prefecture in df.index:
    df_home = df.loc[home_prefecture, years]

    # 増減倍率を計算
    increase_ratios = df_home.pct_change()

    # 折れ線グラフを作成
    increase_ratios.plot(marker="o", figsize=(10, 6), title=f"{home_prefecture}の各年代増減倍率")
    plt.ylabel("増減倍率")
    plt.xlabel("年代")
    plt.xticks(range(len(years)), years)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print(f"都道府県 '{home_prefecture}' がデータに存在しません。")

