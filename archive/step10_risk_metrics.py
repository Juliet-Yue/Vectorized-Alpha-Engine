import pandas as pd  #引入工具
import matplotlib.pyplot as plt

#列表，索引，时间格式
df = pd.read_csv('net_value_final.csv', encoding='utf-8-sig',index_col='日期', parse_dates=['日期'])   #读取并列表


df = df.rename(columns={
    "茅台累计净值": "Benchmark_Net_Value",
    "策略累计净值": "Strategy_Net_Value",
    "日期":"Date"
})


df['Strategy_Cummax'] = df['Strategy_Net_Value'].cummax()


df['Strategy_Drawdown'] = (df["Strategy_Net_Value"] - df["Strategy_Cummax"]) / df["Strategy_Cummax"]


print(df['Strategy_Drawdown'].min())




# 画图：两根曲线放同一张图
df[["Benchmark_Net_Value", "Strategy_Net_Value"]].plot()


# 保存图片
plt.savefig("/home/asd_a/quant-learning/performance_EN.png")

