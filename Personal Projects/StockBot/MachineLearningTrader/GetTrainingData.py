# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:45:12 2026

@author: 789wi
"""

###- Import Statements
from MachineLearningTrader import configML

# Alpaca Imports
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import Adjustment

# Pandas Imports
import pandas as pd

###-


###- Functions
def Get_Candles(symbol, start_time, end_time):
    data_client = StockHistoricalDataClient(configML.CONST_ALPACA_KEY_MAIN, configML.CONST_ALPACA_SECRET_MAIN)
    
    
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol, #"AAPL",
        timeframe=TimeFrame.Day,
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
            "close": float(bar.close),
            "volume": int(bar.volume)
            })
    
    df = pd.DataFrame(data)
    df["time"] = pd.to_datetime(df["time"])
    
    return df

def Create_Training_CSV(data_frame, file_name):
    
    data_frame = data_frame.sort_values('time')
    data_frame = data_frame.drop_duplicates(subset='time')
    data_frame = data_frame.reset_index(drop=True)
    
    
    ## Plot closing price
    #plt.figure(figsize=(15, 6))
    #plt.plot(data_frame["time"], data_frame["close"], linewidth=1)
    #
    #plt.title("Price Over Time")
    #plt.xlabel("Time")
    #plt.ylabel("Price")
    #plt.grid(True, alpha=0.3)
    #
    #plt.tight_layout()
    #plt.show()
    
    data_frame.to_csv(file_name, index=False)
###-


###- Main Program Loop
#print("Getting candles...")
#df = Get_Candles("AAPL", datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")))
#print("Creating CSV and plotting...")
#Create_Training_CSV(df, "TrainCandles.csv")
#print("CSV and plot created successfully!")
###-