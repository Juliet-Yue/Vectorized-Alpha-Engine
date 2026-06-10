import pandas as pd
import numpy as np#引入工具

df = pd.read_csv('features_daily.csv', encoding='utf-8-sig')#列表

df['茅台_看多信号'] = np.where(df['茅台5日均线'] > df['茅台20日均线'], 1, 0)#金叉，多头排列


#保存路径
df.to_csv('/home/asd_a/quant-learning/signals_daily.csv', index=False, encoding='utf-8-sig')