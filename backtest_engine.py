import pandas as pd  #引入工具
import numpy as np
import matplotlib.pyplot as plt


class VectorizedBacktester:

    def __init__(self, data_df,target_col,cost_rate=0.002):
        self.df = data_df.copy()
        self.target_col = target_col
        self.cost_rate = cost_rate
#def定义，先占位
    def generate_signals(self,short_window,long_window):
    # 计算每日涨跌幅（收益率）
            df = self.df
            df['Asset_Return'] = df[self.target_col].pct_change()#资产收益率，目标列

            df['Volatility'] = df['Asset_Return'].rolling(window=short_window).std()#短期滚动标准差
    #均线
            df['MA_Short']=df[self.target_col].rolling(window=short_window).mean()
            df['MA_Long']=df[self.target_col].rolling(window=long_window).mean()

   


    #金叉，多头排列
            df['Signal'] = np.where((df['MA_Short'] > df['MA_Long'])&(df['Volatility'] < 0.025), 1, 0)
    


            df["Position"] = df["Signal"].shift(1)

           

            df['Trade_Action'] = df['Position'].diff().abs().fillna(0)
  
            df['Strategy_Return'] = (df['Position'] * df['Asset_Return']) - (df['Trade_Action'] * self.cost_rate)#策略每日收益，仓位

            df["accumulated_net_asset_value"] = (1 + df["Asset_Return"]).cumprod()#资产累计净值

            df["Strategy_Net_Value"] = (1 + df["Strategy_Return"]).cumprod()#策略累计净值，策略每日收益
            self.df=df


    def calculate_metrics(self):
        ret_mean = self.df['Strategy_Return'].mean()
        ret_std = self.df['Strategy_Return'].std()
        sharpe = np.sqrt(252) * ret_mean / ret_std

        cummax = self.df['Strategy_Net_Value'].cummax()
        drawdown = (self.df['Strategy_Net_Value'] - cummax) / cummax
        cummax = self.df['Strategy_Net_Value'].cummax()
        drawdown = (self.df['Strategy_Net_Value'] - cummax) / cummax
        max_dd  = drawdown.min()

        print(f"组合夏普分布：{sharpe:.3f}\n组合最大回撤：{max_dd:.2%}")      
        return sharpe, max_dd 


df = pd.read_csv('data/merged_daily.csv', encoding='utf-8-sig')

result_maotai = VectorizedBacktester(df, target_col='茅台收盘', cost_rate=0.002)
result_pingan = VectorizedBacktester(df, target_col='平安收盘', cost_rate=0.002)


result_maotai.generate_signals(short_window=5, long_window=20)
result_pingan.generate_signals(short_window=5, long_window=20)


result_maotai.calculate_metrics()
result_pingan.calculate_metrics()




df_portfolio = pd.DataFrame()

df_portfolio['Maotai_Ret'] = result_maotai.df['Strategy_Return']
df_portfolio['Pingan_Ret'] = result_pingan.df['Strategy_Return']

df_portfolio['Portfolio_Ret'] = df_portfolio[['Maotai_Ret', 'Pingan_Ret']].mean(axis=1)
df_portfolio['Portfolio_Net_Value'] = (1 + df_portfolio['Portfolio_Ret']).cumprod()


