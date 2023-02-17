import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('../data/test.csv')
print(df)

# # 検索条件を指定する
# print(df.columns)
# print(df[df['年齢'] < 40])
# print(df[df[['年齢' < 40]] & df[('性別' == '男性')])
print(df[['年齢', '名前']][(df['年齢'] < 40) & (df['性別'] == '男性')])

# locを使って検索条件を指定
# print(df.loc[df['年齢'] < 40])
print(df.loc[(df['年齢'] < 40) & (df['性別'] == '男性'), ['名前', '年齢']])
print(df.loc[['年齢', '名前']])