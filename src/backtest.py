from iterative_base import IterativeBase

class Backtest(IterativeBase):

    def __init__(self, symbol, start, end, amount, sl_perc=None, tp_perc=None, use_spread=True):
        super().__init__(symbol, start, end, amount, use_spread)  # Initialize parent attributes
        self.sl_perc = sl_perc  # Add stop-loss percentage
        self.tp_perc = tp_perc  # Add take-profit percentage
        self.entry_price = None  # Track position entry price

    # helper method for buy position
    def go_long(self, bar, units = None, amount = None):
        date, price, spread = self.get_values(bar)
        self.entry_price = price  # Record entry price for SL/TP calculation
        if self.position == -1:
            self.buy_instrument(bar, units = -self.units) # if short position, go neutral first
        if units:
            self.buy_instrument(bar, units = units)
        elif amount:
            if amount == "all":
                amount = self.current_balance
            self.buy_instrument(bar, amount = amount) # go long
        self.entry_price = price  # Record entry price for SL/TP calculation
        self.position = 1

    # helper method for sell position
    def go_short(self, bar, units = None, amount = None):
        date, price, spread = self.get_values(bar)
        if self.position == 1:
            self.sell_instrument(bar, units = self.units) # if long position, go neutral first
        if units:
            self.sell_instrument(bar, units = units)
        elif amount:
            if amount == "all":
                amount = self.current_balance
            self.sell_instrument(bar, amount = amount) # go short
        self.entry_price = price  # Record entry price for SL/TP calculation
        self.position = -1

    #Adding stop loss and take profit conditions
    def check_sl_tp(self, bar, price, date):
        # print(f"DEBUG | Position: {self.position}, Entry Price: {self.entry_price}, SL Level: {self.entry_price * (1 - self.sl_perc)}, TP Level: {self.entry_price * (1 + self.tp_perc)}, Current Price: {price}")
        """
        Checks for Stop Loss (SL) and Take Profit (TP) conditions.
        Closes the position if either condition is met.
        """
        date, price, spread = self.get_values(bar)

        if self.position == 0:
            return

        elif self.position == 1:  # Long position
            if self.tp_perc and price >= self.entry_price * (1 + self.tp_perc):  # TP hit
                self.sell_instrument(bar, units=self.units)
                print(f"{date} | Take Profit hit for LONG position at {price}")
                self.position = 0
                
            elif self.sl_perc and price <= self.entry_price * (1 - self.sl_perc):  # SL hit
                self.sell_instrument(bar, units=self.units)
                print(f"{date} | Stop Loss hit for LONG position at {price}")
                self.position = 0
                
        elif self.position == -1:  # Short position
            if self.tp_perc and price <= self.entry_price * (1 - self.tp_perc):  # TP hit
                self.buy_instrument(bar, units=-self.units)
                print(f"{date} | Take Profit hit for SHORT position at {price}")
                self.position = 0
                
            elif self.sl_perc and price >= self.entry_price * (1 + self.sl_perc):  # SL hit
                self.buy_instrument(bar, units=-self.units)
                print(f"{date} | Stop Loss hit for SHORT position at {price}")
                self.position = 0

                
        # Update position column in the DataFrame
        self.data.loc[self.data.index[bar], 'position'] = self.position    




    def test_sma_strategy(self, SMA_S, SMA_M, SMA_L):
        
        # nice printout
        stm = "Testing SMA strategy | {} | SMA_S = {}, SMA_M = {} & SMA_L = {}".format(self.symbol, SMA_S, SMA_M ,SMA_L)
        print("-" * 75)
        print(stm)
        print("-" * 75)
        
        # reset 
        self.position = 0  # initial neutral position
        self.trades = 0  # no trades yet
        self.current_balance = self.initial_balance  # reset initial capital
        self.get_data() # reset dataset
        
        # prepare data
        self.data["SMA_S"] = self.data["price"].rolling(SMA_S).mean()
        self.data["SMA_M"] = self.data["price"].rolling(SMA_M).mean()
        self.data["SMA_L"] = self.data["price"].rolling(SMA_L).mean() 
        self.data.dropna(inplace = True)

        # Initialize position column
        self.data['position'] = 0

        # sma crossover strategy
        for bar in range(len(self.data)-1): # all bars (except the last bar)
            date, price, spread = self.get_values(bar)

            if self.position == 0:
                if self.data["SMA_S"].iloc[bar] > self.data["SMA_M"].iloc[bar] > self.data["SMA_L"].iloc[bar]: # signal to go long
                    if self.data["price"].iloc[bar] > self.data["SMA_S"].iloc[bar]:
                        self.go_long(bar, amount = "all") # go long with full amount
                        self.position = 1  # long position
                    
                elif self.data["SMA_S"].iloc[bar] < self.data["SMA_M"].iloc[bar] < self.data["SMA_L"].iloc[bar]: # signal to go short
                    if self.data["price"].iloc[bar] < self.data["SMA_S"].iloc[bar]:
                        self.go_short(bar, amount = "all") # go short with full amount
                        self.position = -1 # short position
                    
            # Update position column in the DataFrame
            self.data.loc[self.data.index[bar], 'position'] = self.position   

            self.check_sl_tp(bar, price, date)

        self.close_pos(bar+1) # close position at the last bar

        # Ensure the final position is logged
        self.data.loc[self.data.index[-1], 'position'] = 0

