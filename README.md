# Vectorized OOP Backtesting Engine (面向对象的多资产向量化回测引擎)

这是一个轻量级、高度解耦的面向对象（OOP）量化交易回测框架，专为快速验证多资产的中低频（日级/分钟级）交易信号与策略组合设计。

本项目彻底推翻了传统单脚本线性处理的局限，有效解决了 Pandas 向量化回测中由于无状态机制导致的 **"向量化失忆症 (Vectorized Amnesia)"** 与 **"状态穿透"** 等常见工程陷阱。

---

## ⚙️ 核心系统架构 (System Architecture)

- **面向对象模块化封装 (OOP Architecture)**：将数据接入、信号生成（`generate_signals`）与绩效度量（`calculate_metrics`）解耦封装于独立的 `VectorizedBacktester` 类，核心逻辑之间高内聚低耦合。
- **持久化状态隔离 (State Persistence)**：利用类属性（`self`）维护单资产的独立持仓、专属账本（`self.df`）与交易费率等持久化状态，为未来扩展路径依赖型止损（如追踪止损、滚动最高点出局）提供完美的工程根基。
- **投资组合级组装 (Portfolio Construction)**：支持批量实例化独立资产的交易对象（互不干扰、并行维护独立买卖点），并在类外部无缝拼装为复合投资组合（Portfolio Allocation），计算多资产等权/加权综合净值。

---

## ✨ 关键特性 (Core Features)

- **高性能向量化计算**：核心指标计算（均线交叉、滚动波动率等）全面基于 NumPy 和 Pandas 的向量化矩阵运算，摒弃低效的 `for` 循环，具备极高的数据处理效率。
- **多维风控过滤模块**：内置移动波动率风控机制。在双均线金叉多头排列信号之上，引入短期滚动标准差（Volatility）约束，用于在震荡市或剧烈波动市场中实施风控拦截，滤除假突破。
- **真实的交易摩擦成本模拟**：严格拒绝理想化回测。通过对每日仓位变化（`Trade_Action`）的变动捕获，在策略收益率中严格扣除单边千分之二（可自定义）的手续费与滑点损耗，确保回测绩效的实盘指导价值。

---

## 📊 策略绩效展示 (Performance Review)

* **测试标的**：贵州茅台 (600519) + 中国平安 (601318) 等权组合
* **核心逻辑**：双均线金叉过滤 + 移动波动率约束滤波
* **资产曲线**：项目已实现组合净值自动化计算（数据已分类规整至 `data/` 目录）

> 💡 **项目提示**：策略多指标评估函数（`calculate_metrics`）已实现年化夏普比率（Sharpe Ratio）与最大回撤（Max Drawdown）的自动化清洗与打印。

*(具体的绩效曲线图片已安全存放在 `assets/` 目录中)*

---

## 🚀 快速开始 (Quick Start)

```python
import pandas as pd
from backtest_engine import VectorizedBacktester

# 1. 载入清洗完成的合并多资产数据集
data_df = pd.read_csv('data/merged_daily.csv', encoding='utf-8-sig')

# 2. 实例化引擎：分别为两只股票雇佣独立的交易员，并配置千分之二真实手续费
result_maotai = VectorizedBacktester(data_df, target_col='maotai_close', cost_rate=0.002)
result_pingan = VectorizedBacktester(data_df, target_col='pingan_close', cost_rate=0.002)

# 3. 驱动工具箱：生成交易信号与模拟历史持仓变化
result_maotai.generate_signals(short_window=5, long_window=20)
result_pingan.generate_signals(short_window=5, long_window=20)

# 4. 汇报业绩：打印各自的夏普比率与最大回撤
result_maotai.calculate_metrics()
result_pingan.calculate_metrics()
