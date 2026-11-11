###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#import GetTrainingData as get_data
from MachineLearningTrader.Pct_Model import Train_Pct as train

#from datetime import datetime, timedelta as dt
#from zoneinfo import ZoneInfo
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Predict(model, df, lookback_days=30, forecast_days=30):
    current_window = list(df['pct_close'].iloc[-lookback_days:].values)
    
    predicted_pct_changes = []
    
    for i in range(forecast_days):
        # Reshape current_window to fit scikit-learn's expected input shape (1, 30)
        input_features = np.array(current_window).reshape(1, -1)
        
        # Predict the next day's percent change
        next_day_pred = model.predict(input_features)[0]
        predicted_pct_changes.append(next_day_pred * random.random())
        
        # Update the window: slide it forward by removing the oldest and adding the prediction
        current_window.pop(0)
        current_window.append(next_day_pred)
        
    current_price_list = []
    future_price_list = []
    
    for i in range(len(df)):
        current_price_list.append(df['close'].iloc()[i])
    
    for i in range(len(predicted_pct_changes)):
        if(i == 0):
            future_price_list.append(current_price_list[-1] * (1+predicted_pct_changes[i]))
        else:
            future_price_list.append(future_price_list[i-1] * (1+predicted_pct_changes[i]))
        
        
    return predicted_pct_changes, future_price_list
    

def Plot_Predictions(df, future_price_list, ticker, forecast_days=30):
    #df_future = df.copy()
        
    last_date = df.index[-1]
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=forecast_days)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Historical Close Price')
    plt.plot(future_dates, future_price_list, label='Predicted Future Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Pct {ticker} Stock Price Prediction')
    plt.legend()
    plt.show()
        
    

def Run_Bot(stock_data_path, ticker, lookback_days=30, forecast_days=30, PLOT=True):
    ## Load Training Data
    # If erroring, check imports
    #print("Getting candles...")
    #candles_df = get_data.Get_Candles("AAPL", datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")) - dt(hours=1))
    #print("Creating CSV and plotting...")
    #get_data.Create_Training_CSV(candles_df, "TrainCandles.csv")
    #print("CSV and plot created successfully!\n\n")
    
    # Prepare Data
    stock_data = train.Load_Stock_Data(stock_data_path)
    x, y, df = train.Prepare_Data(stock_data, lookback_days)
    
    # Train Model
    model, metrics = train.Train_Model(x, y)
    
    # Make and Chart Prediction
    future_predictions, future_price_list = Predict(model, df, lookback_days, forecast_days)
    #future_earnings = future_predictions[-1]
    
    if PLOT:
        Plot_Predictions(df, future_predictions, ticker, forecast_days)
    
    print(f'{forecast_days}-Day earnings are {future_price_list[-1] - df['close'].iloc()[-1]:.2f} (from a price of {df['close'].iloc()[-1]:.2f} to {future_price_list[-1]:.2f}), with a return of {((future_price_list[-1] / df['close'].iloc()[-1]) - 1) * 100:.2f}%')
    
    return float(future_predictions[-1]), float(future_price_list[-1]), float(df['close'].iloc[-1]), metrics