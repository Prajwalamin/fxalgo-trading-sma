from backtest import Backtest
from config import DEFAULT_SYMBOL, START_DATE, END_DATE, INITIAL_BALANCE, USE_SPREAD, sl_perc, tp_perc
from utils import plot_data

if __name__ == "__main__":
    # Initialize the backtesting instance
    backtest = Backtest(DEFAULT_SYMBOL, START_DATE, END_DATE, INITIAL_BALANCE, sl_perc, tp_perc, USE_SPREAD)

    # Run the SMA Crossover Strategy
    backtest.test_sma_strategy(21, 50, 200)

    # Plot the data
    plot_data(backtest.data)