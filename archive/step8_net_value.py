import pandas as pd #引入工具

df = pd.read_csv('strategy_returns.csv', encoding='utf-8-sig')   #读取并列表


df["茅台累计净值"] = (1 + df["茅台收益率"]).cumprod()

df["策略累计净值"] = (1 + df["策略每日收益"]).cumprod()



#保存路径
df.to_csv('/home/asd_a/quant-learning/net_value_final.csv', index=False, encoding='utf-8-sig')