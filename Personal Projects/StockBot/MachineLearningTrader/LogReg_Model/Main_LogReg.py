###- Import Statements
import numpy as np
import matplotlib.pyplot as plt

#import GetTrainingData as get_data
from MachineLearningTrader.LogReg_Model import Train_LogReg as train

#from datetime import datetime, timedelta as dt
#from zoneinfo import ZoneInfo

#import random
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Predict(model, df, forecast_days=30):
    
    current_window = np.column_stack([
        df['pct_open'].iloc[-forecast_days:].values,
        df['pct_close'].iloc[-forecast_days:].values,
        df['pct_high'].iloc[-forecast_days:].values,
        df['pct_low'].iloc[-forecast_days:].values,
        
        df['daily_return'].iloc[-forecast_days:].values,
        df['log_return'].iloc[-forecast_days:].values,
        
        df['sma_5_ratio'].iloc[-forecast_days:].values,
        df['ema_5_ratio'].iloc[-forecast_days:].values,
        df['sma_10_ratio'].iloc[-forecast_days:].values,
        df['ema_10_ratio'].iloc[-forecast_days:].values,
        df['sma_20_ratio'].iloc[-forecast_days:].values,
        df['ema_20_ratio'].iloc[-forecast_days:].values,
        
        df['rsi_14'].iloc[-forecast_days:].values,
        df['macd'].iloc[-forecast_days:].values,
        df['macd_signal'].iloc[-forecast_days:].values,
        df['macd_hist'].iloc[-forecast_days:].values,
        
        df['return_lag_1'].iloc[-forecast_days:].values,
        df['return_lag_2'].iloc[-forecast_days:].values,
        df['return_lag_3'].iloc[-forecast_days:].values,
        df['return_lag_5'].iloc[-forecast_days:].values,
        df['return_lag_10'].iloc[-forecast_days:].values,

        
        df['volume_pct_change'].iloc[-forecast_days:].values,
        df['relative_volume'].iloc[-forecast_days:].values,
        df['obv_pct_change'].iloc[-forecast_days:].values,
        df['cmf_20'].iloc[-forecast_days:].values,
        
        df['volume_change_lag_1'].iloc[-forecast_days:].values,
        df['volume_change_lag_2'].iloc[-forecast_days:].values,
        df['volume_change_lag_3'].iloc[-forecast_days:].values,
        df['volume_change_lag_5'].iloc[-forecast_days:].values,
        df['volume_change_lag_10'].iloc[-forecast_days:].values
    ])
        
    input_features = np.array(current_window).reshape(1, -1)
    
    # Predict the x days' percent change
    predicted_pct_up = model.predict_proba(input_features)[0, 1]
    return predicted_pct_up
    

def Run_Bot(stock_data_path, forecast_days=30):
    # Load Training Data
    # If erroring, check imports
    #print("Getting candles...")
    #candles_df = get_data.Get_Candles("AAPL", datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")) - dt(hours=1))
    #print("Creating CSV and plotting...")
    #get_data.Create_Training_CSV(candles_df, "TrainCandles.csv")
    #print("CSV and plot created successfully!\n\n")
    
    # Prepare Data
    stock_data = train.Load_Stock_Data(stock_data_path)
    x, y, df = train.Prepare_Data(stock_data, forecast_days)
    
    # Train Model
    model, metrics = train.Train_Model(x, y, forecast_days)
    
    # Make and Chart Prediction
    predicted_pct_up = Predict(model, df, forecast_days)
    
    
    # No longer need to plot predictions since we are not predicting a future value
    print(f'{forecast_days}-Day Returns have a predicted {predicted_pct_up * 100:.2f}% chance of being positive.')
    
    return float(predicted_pct_up), float(df['close'].iloc[-1]), metrics