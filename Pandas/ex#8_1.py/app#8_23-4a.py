import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# csvファイルをデータフレームに読み込む
filename = "tokyo.csv"
df = pd.read_csv(filename, header=None, encoding="shift_jis", dtype=str)

# 住所（2の列）が“1130021”の住所を抽出して表示
results = df[df[2] == "1130021"]
print(results[[2,6,7,8]])
