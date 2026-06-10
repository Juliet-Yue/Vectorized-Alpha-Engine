import pandas as pd #引入工具

df = pd.read_csv('signals_daily.csv', encoding='utf-8-sig')   #读取并列表


df["实际持仓"] = df["茅台_看多信号"].shift(1)#下移一行


df['策略每日收益'] = df['实际持仓'] * df['茅台收益率']#新加一行


# 删除含有 NaN 的行
df_clean=df .dropna()



#保存路径
df.to_csv('/home/asd_a/quant-learning/strategy_returns.csv', index=False, encoding='utf-8-sig')