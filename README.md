# SMA Crossover Bot

🚀 A Python-based algorithmic backtesting tool that evaluates a **Simple Moving Average (SMA) Crossover Strategy** using historical data.

---

## Features

- 📈 **Dual Moving Average Crossover**: Identifies entry and exit points based on short-term and long-term moving averages.
- 🛠️ **Configurable Parameters**:
  - Short SMA Period (`SMA_S`)
  - Short SMA Period (`SMA_M`)
  - Long SMA Period (`SMA_L`)
  - Stop Loss (`sl_perc`) and Take Profit (`tp_perc`) percentages.
- 💵 **Backtesting**: Evaluate strategy performance on EURUSD historical data.
- 📊 **Performance Metrics**: Tracks net asset value (NAV), trades executed, and overall strategy performance.

---

## How It Works

1. **SMA Crossover Strategy**:
   - **Buy Signal**: When all the SMAs are one above each other, the bot places a buy order.
   - **Sell Signal**:When all the SMAs are one below each other, the bot places a sell order.

2. **Stop Loss & Take Profit**:
   - Protect profits and limit losses by automatically exiting positions based on predefined percentages.

3. **Backtesting**:
   - Simulate trades using historical data to evaluate the strategy before live deployment.

---

## Future Enhancements (In Progress)

- 🚀 **Optimization**: Implement automatic optimization of strategy parameters like SMA periods, stop loss, and take profit percentages.
- 🧠 **Machine Learning**: Explore machine learning algorithms to fine-tune the strategy and identify patterns that are not captured by simple moving averages.
- 📉 **Live Trading Integration**: Integrate with live trading platforms (e.g., Oanda, Interactive Brokers) for real-time execution of trades based on the strategy.
- 📊 **Advanced Performance Metrics**: Add risk-adjusted return metrics like Sharpe ratio and drawdown analysis.
- 🔄 **Multiple Strategy Support**: Implement support for testing multiple strategies (e.g., EMA crossover, MACD) and compare their performance.
- 📈 **Advanced Visualization**: Provide more advanced graphical outputs such as trade visualization on price charts, equity curve, and strategy performance metrics.
- 💾 **Data Storage & Analysis**: Implement functionality to log and store backtest results for future analysis, performance tracking, and optimization.

---

## Limitations

- This version supports **backtesting only**. It does not connect to live markets yet.
- Historical data should include columns for price and spread (e.g., `detailed.csv`).
- The strategy is based on the **SMA crossover** logic, which may not be suitable for all market conditions.
- **Data availability**: The backtesting relies on having accurate and complete historical data for the given symbol and time period.
- **No risk management**: While stop loss and take profit are implemented, more advanced risk management strategies (e.g., position sizing, drawdown control) are not yet integrated.
- This bot does not **optimize parameters** automatically and requires manual parameter tuning for optimal results.
- This bot is still under development and hasn't yet achieved profitability at the moment.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

