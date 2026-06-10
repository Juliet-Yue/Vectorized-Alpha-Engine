import pandas as pd #引入工具
import matplotlib.pyplot as plt


df = pd.read_csv('net_value_final.csv', encoding='utf-8-sig',index_col='日期', parse_dates=['日期'])   #读取并列表

# 画图：两根曲线放同一张图
df.plot( y=["茅台累计净值", "策略累计净值"], kind="line")


# 保存图片
plt.savefig("/home/asd_a/quant-learning/strategy_performance.png")

