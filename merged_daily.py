import pandas as pd
#引入表格工具
df_maotai= pd.read_csv('data/guizhou_maotai_daily.csv', encoding='utf-8-sig')
df_pingan= pd.read_csv('data/pingan_601318.csv', encoding='utf-8-sig')
#提取数据变成DataFrame
df_maotai = df_maotai[['日期', '收盘']]
df_pingan = df_pingan[['日期', '收盘']]
#提取需要两列
df_maotai.rename(columns={'收盘': '茅台收盘'}, inplace=True)
df_pingan.rename(columns={'收盘': '平安收盘'}, inplace=True)
#改名
merged = pd.merge(df_maotai,df_pingan , on='日期', how='inner')
#合并表格
merged.to_csv("data/merged_daily.csv", index=False, encoding="utf-8-sig")
#保存路径