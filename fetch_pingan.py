import akshare as ak #akshare股票数据库
import pandas as pd  #pandas是python里的excel                                   #1引入数据和工具

df = ak.stock_zh_a_hist ( #df是DataFrame,是pandas里面的一张表格
                         #ak里面的,stock_zh_a_hist中国A股历史数据，固定格式
    #确定股票需要的5个基本数据
    symbol="601318",    # 把 600519 改成 601318（中国平安代码）    #股票代码
    period="daily",     #周期                                                   #2确定股票基本信息，列表
    start_date="20200317",  # 5年前的今天（2020-03-17）
    end_date="20250317",    # 今天（2025-03-17）    时间开始结束
    adjust="hfq"        #复权，除去分红等事件，使K线更连贯，更好的反应盈利和走势
                        #后复权，前复权，不复权
)

df=df[["日期","开盘","最高","最低","收盘","成交量"]]                               #3提取目标数据


df.to_csv(
    "data/pingan_601318.csv", index=False, encoding='utf-8-sig'   # 保存到 data 文件夹，名字改规范
)