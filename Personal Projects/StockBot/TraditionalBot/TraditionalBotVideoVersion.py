# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:38:04 2026

@author: 789wi

To Do:
    -Create a sell function with expiry
    -Potentially take in longer time spans for buy and sell orders
    -Check multiple stocks
    
Completed:    
    -*-Fix bot runtime functionality so that this can be used every 15 minutes as intended (apparently this can use alpaca.data.historical still if this is fetched constantly)
"""

###- Import Statements
import configBot
import holidays as holidays
from datetime import datetime, time, timedelta as dt
from zoneinfo import ZoneInfo

# Alpaca Imports
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import Adjustment

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.requests import TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

# Pandas Imports
import pandas as pd
import pandas_ta_classic as ta
###-


###- Functions 
# This will get historical data candles
# Currently set to get data for each minute
def Get_Candles(symbol, start_time, end_time):
    data_client = StockHistoricalDataClient(configBot.CONST_ALPACA_KEY, configBot.CONST_ALPACA_SECRET)
    
    
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol, #"AAPL",
        timeframe=TimeFrame.Minute,
        start=start_time, #datetime(2026, 10, 1),
        end=end_time, #datetime(2026, 10, 3)
        adjustment=Adjustment.SPLIT
    )
    
    data = []
    
    bars = data_client.get_stock_bars(request_params)
    
    for bar in bars[symbol]:
        data.append({
            "time": bar.timestamp,
            "open": float(bar.open),
            "high": float(bar.high),
            "low": float(bar.low),
            "close": float(bar.close)
            #,"volume": int(bar.volume) # This can be added after
            })
    
    df = pd.DataFrame(data)
    df["time"] = pd.to_datetime(df["time"])
    
    return df


def Calculate_Indicators(data_frame):
    # EMAs
    data_frame["EMA_5"] = ta.ema(data_frame["close"], length=5)
    data_frame["EMA_8"] = ta.ema(data_frame["close"], length=8) 

    # ATR
    data_frame["ATR_14"] = ta.atr(data_frame["high"], data_frame["low"], data_frame["close"], length=14)
    
    return data_frame


# This defines the strategy logic
def EMA_Crossover(symbol, data_frame):
    take_profit_ratio = 1.5
    
    # Check if the 5-period EMA crosses above the 8 period EMA
    last_candle = data_frame.iloc[-1]
    previous_candle = data_frame.iloc[-2]
    
    # Crossover Buy Signal (EMA 5 crosses above EMA 8)
    if last_candle['EMA_5'] > last_candle['EMA_8'] and previous_candle['EMA_5'] < previous_candle['EMA_8']:
        print("Buy Signal: EMA 5 crossed above EMA 8")
        entry_price = last_candle['close']
        stop_loss = entry_price - last_candle['ATR_14']
        stop_distance = entry_price - stop_loss
        take_profit = entry_price + (stop_distance * take_profit_ratio)
        Place_Order(symbol, stop_loss, take_profit)
    else:
        print("Strategy conditions not met")


def Place_Order(symbol, stop_loss_in, take_profit_in):
    trading_client = TradingClient(configBot.CONST_ALPACA_KEY, configBot.CONST_ALPACA_SECRET)
    
    quantity = 1
    
    market_order_data = MarketOrderRequest(
        symbol=symbol, 
        qty=quantity, 
        side=OrderSide.BUY, #Buying or selling
        time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
        order_class=OrderClass.BRACKET,
        take_profit=TakeProfitRequest(limit_price=take_profit_in),
        stop_loss=StopLossRequest(stop_price=stop_loss_in)
        )
    
    market_order = trading_client.submit_order(market_order_data)
    
    #print(market_order)
    
    # Print success/failure message depending on the order placement status
    if market_order.failed_at == None:
        print(f"Market order successfully placed for {symbol}. Stop loss is: {stop_loss_in}. Take profit is: {take_profit_in}.")
    else:
        print(f"Market order placement for {symbol} failed.")


def Run_Bot():
    print("Starting trading bot...")
    
    last_checked = None
    symbol = "AAPL"
    print(f"Symbol for trading is: {symbol}")
        
    while True:
        current_time_ny = datetime.now(ZoneInfo("America/New_York"))
        
        # Check that the market is open
        if (current_time_ny.weekday() >= 5) or (current_time_ny.date() in holidays.UnitedStates()) or not (time(9, 30) <= current_time_ny.time() <= time(16, 0)):
            print("The markets are closed...")
            continue
            
        # Check for a new 15 minute candle
        if current_time_ny.minute % 1 == 0 and current_time_ny.second < 10:
            # Check if the 15 minute interval has changed since the last check
            if last_checked != current_time_ny.minute:
                print("Checking for trade signals...")
                price = Get_Candles(symbol, current_time_ny - dt(minutes=15), current_time_ny)
                price = Calculate_Indicators(price)
                EMA_Crossover(price)
                last_checked = current_time_ny.minute
                
        time.sleep(10)
###-


###-: Main Code
Run_Bot()