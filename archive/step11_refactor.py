import pandas as pd  #引入工具
import numpy as np


#def定义，先占位
def run_backtest(df,target_col, short_window, long_window):   
    # 计算每日涨跌幅（收益率）
    df['茅台收益率'] = df['茅台收盘'].pct_change()
    #均线
    df['茅台5日均线']=df['茅台收盘'].rolling(window=short_window).mean()
    df['茅台20日均线']=df['茅台收盘'].rolling(window=long_window).mean()

    #金叉，多头排列
    df['茅台_看多信号'] = np.where(df['茅台5日均线'] > df['茅台20日均线'], 1, 0)
    
    #下移一行
    df["实际持仓"] = df["茅台_看多信号"].shift(1)

    #新加一行
    df['策略每日收益'] = df['实际持仓'] * df['茅台收益率']

    df["茅台累计净值"] = (1 + df["茅台收益率"]).cumprod()

    df["策略累计净值"] = (1 + df["策略每日收益"]).cumprod()

    df = df.rename(columns={
    "茅台累计净值": "Benchmark_Net_Value",
    "策略累计净值": "Strategy_Net_Value",
    "策略每日收益":"Strategy_Return",
    "实际持仓":"Position",
    "茅台_看多信号":"Signal",
    "茅台5日均线":"Mao5",
    "茅台20日均线":"Mao20",
    "茅台收益率":"Benchmark_Return",
    })

    return df

df = pd.read_csv('/home/asd_a/quant-learning/merged_daily.csv', encoding='utf-8-sig')#列表



result_1 = run_backtest(df.copy(),5,20)
result_2 = run_backtest(df.copy(),10,30)
result_3 = run_backtest(df.copy(),3,15)

print("参数5-20最终净值:",result_1['Strategy_Net_Value'].iloc[-1])
print('参数10-30最终净值:',result_2['Strategy_Net_Value'].iloc[-1])
print("参数3-15最终净值:",result_3['Strategy_Net_Value'].iloc[-1])