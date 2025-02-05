import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

# csvファイルをデータフレームに読み込む
filename = "tokyo.csv"
df = pd.read_csv(filename, header=None, encoding="shift_jis", dtype=str)

# 住所（8の列）が“本駒込”に一致した住所を抽出
results = df[df[8] == "本駒込"]
print("\n", results[[2,6,7,8]])

# 住所（8の列）に“本駒込”が含まれる住所を抽出
results = df[df[8].str.contains("本駒込")]
print("\n", results[[2,6,7,8]])
