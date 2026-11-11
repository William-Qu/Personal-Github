###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import GetTrainingData as get_data
from MachineLearningTrader.Raw_Model import Train_Raw as train

#from datetime import datetime, timedelta as dt
#from zoneinfo import ZoneInfo
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Predict(model, df, lookback_days=30):
    x_future = np.array(df.drop(['prediction'], axis=1))[-lookback_days:]
    future_predictions = model.predict(x_future)
    
    return future_predictions
    

def Plot_Predictions(df, future_predictions, ticker, forecast_days=30):
    #df_future = df.copy()
    
    last_date = df.index[-1]
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=forecast_days)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['close'], label='Historical Close Price')
    plt.plot(future_dates, future_predictions, label='Predicted Future Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Raw {ticker} Stock Price Prediction')
    plt.legend()
    plt.show()
    

def Run_Bot(stock_data_path, ticker, lookback_days=30, forecast_days=30, PLOT=True):
    # Load Training Data
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
    future_predictions = Predict(model, df, forecast_days)
    
    if PLOT:
        Plot_Predictions(df, future_predictions, ticker, forecast_days)
    
    print('Future Price Predictions:')
    print(future_predictions)
    
    print(f'{forecast_days}-Day earnings are {future_predictions[-1] - df['close'].iloc()[-1]:.2f} (from a price of {df['close'].iloc()[-1]:.2f} to {future_predictions[-1]:.2f}), with a return of {((future_predictions[-1] / df['close'].iloc()[-1]) - 1) * 100:.2f}%')
    
    return float((future_predictions[-1] / df['close'].iloc()[-1]) - 1), float(future_predictions[-1]), float(df['close'].iloc[-1]), metrics