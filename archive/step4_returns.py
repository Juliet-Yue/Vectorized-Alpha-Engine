import pandas as pd#引用工具

df_returns= pd.read_csv('merged_daily.csv', encoding='utf-8-sig')#列表DateFrame


# 计算每日涨跌幅（收益率），默认与前一天对比
df_returns['茅台收益率'] = df_returns['茅台收盘'].pct_change()
df_returns['平安收益率'] = df_returns['平安收盘'].pct_change()


  
# 删除含有 NaN 的行
df_clean = df_returns.dropna()


df_clean.to_csv('/home/asd_a/quant-learning/returns_daily.csv', index=False, encoding='utf-8-sig')