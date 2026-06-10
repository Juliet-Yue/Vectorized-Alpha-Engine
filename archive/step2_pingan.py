import akshare as ak
import pandas as pd
# 1. 获取pingan的历史日线数据
# adjust="hfq" 表示后复权（更适合长期分析），如果不要复权可以写 adjust=""
df = ak.stock_zh_a_hist(
    symbol="601318",
    period="daily",
    start_date="20200317",  # 5年前的今天（2020-03-17）
    end_date="20250317",    # 今天（2025-03-17）
    adjust=""
)

# 2. 只保留我们需要的列：开、高、低、收、成交量
df = df[["日期", "开盘", "最高", "最低", "收盘", "成交量"]]

# 3. 保存为 CSV 文件（也可以改成 .xlsx 保存为 Excel）
df.to_csv("/home/asd_a/quant-learning/pingan_601318.csv", index=False, encoding="utf-8-sig")
print("✅ 数据已保存为 step2_pingan.csv")
print(f"📊 共获取 {len(df)} 行数据，时间范围：{df['日期'].min()} ~ {df['日期'].max()}")