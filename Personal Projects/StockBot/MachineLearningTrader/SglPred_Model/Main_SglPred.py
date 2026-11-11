###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import GetTrainingData as get_data
from MachineLearningTrader.SglPred_Model import Train_SglPred as train

#from datetime import datetime, timedelta as dt
#from zoneinfo import ZoneInfo

#import random
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Predict(model, df, lookback_days=30):
    
    current_window = np.column_stack([
        df['pct_open'].iloc[-lookback_days:].values,
        df['pct_close'].iloc[-lookback_days:].values,
        df['pct_high'].iloc[-lookback_days:].values,
        df['pct_low'].iloc[-lookback_days:].values
    ])
        
    input_features = np.array(current_window).reshape(1, -1)
    
    # Predict the x days' percent change
    predicted_pct_change = model.predict(input_features)[0]
    predicted_price = df['close'].iloc[-1] * predicted_pct_change
        
    return predicted_pct_change, predicted_price
    

def Plot_Predictions(df, future_predicted_price, ticker, forecast_days=30):
    
    future_date = df.index[-1] + pd.Timedelta(days=forecast_days)
    
    predicted_line_date = [df.index[-1], future_date]
    predicted_line_price = [df['close'].iloc[-1], future_predicted_price]
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Historical Close Price')
    plt.plot(predicted_line_date, predicted_line_price, label='Predicted Future Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'SglPred {ticker} Stock Price Prediction')
    plt.legend()
    plt.show()
    
    
def Run_Bot(stock_data_path, ticker, lookback_days=30, forecast_days=30, PLOT=True):
    # Load Training Data
    # If erroring, check imports
    #print("Getting candles...")
    #candles_df = get_data.Get_Candles("AAPL", datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")) - dt(hours=1))
    #print("Creating CSV and plotting...")
    #get_data.Create_Training_CSV(candles_df, "TrainCandles.csv")
    #print("CSV and plot created successfully!\n\n")
    
    # Prepare Data
    stock_data = train.Load_Stock_Data(stock_data_path)
    x, y, df = train.Prepare_Data(stock_data, lookback_days,forecast_days)
    
    # Train Model
    model, metrics = train.Train_Model(x, y)

    
    # Make and Chart Prediction
    predicted_pct_change, future_price = Predict(model, df, lookback_days)
    
    if PLOT:
        Plot_Predictions(df, future_price, ticker, forecast_days)
    
    print(f'{forecast_days}-Day earnings are {future_price - df['close'].iloc[-1]:.2f} (predicted price of {future_price:.2f}), with a return of {(predicted_pct_change - 1) * 100:.2f}%')
    
    return float(predicted_pct_change - 1), float(future_price), float(df['close'].iloc[-1]), metrics