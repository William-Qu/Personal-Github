###- Import Statements
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
def Load_Stock_Data(csv_file):
    print('Loading data...')
    df = pd.read_csv(csv_file)
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    return df


def Prepare_Data(df, lookback_days=30):
    print('Preparing data...')    
    df = df[-lookback_days:]
    
    return df


def Calculate_Indicators(data_frame):
    # EMAs
    data_frame["EMA_5"] = ta.ema(data_frame["close"], length=5)
    data_frame["EMA_8"] = ta.ema(data_frame["close"], length=8) 

    # ATR
    data_frame["ATR_14"] = ta.atr(data_frame["high"], data_frame["low"], data_frame["close"], length=14)
    
    return data_frame


# This defines the strategy logic
def EMA_Crossover(ticker, data_frame):
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
        return_percent = take_profit / entry_price
        return entry_price, stop_loss, take_profit, return_percent
    else:
        return 0, 0, 0, 0

###-

def RunBot(stock_data_path, ticker, lookback_days=30):
    # Prepare Data
    stock_data = Load_Stock_Data(stock_data_path)
    df = Prepare_Data(stock_data, lookback_days)
    
    df = Calculate_Indicators(df)
    entry_price, stop_loss, take_profit, return_percent = EMA_Crossover(ticker, df)
    
    print(f'For ticker {ticker} an Entry Price of {entry_price} and a Stop Loss of {stop_loss} is recommended (return of {return_percent - 1})')
    
    return float(entry_price), float(stop_loss), float(take_profit), float(return_percent - 1)

###-: Main Code