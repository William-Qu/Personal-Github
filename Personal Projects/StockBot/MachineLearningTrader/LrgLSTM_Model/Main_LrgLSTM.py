###- Import Statements
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


#import GetTrainingData as get_data
from MachineLearningTrader.LrgLSTM_Model import Train_LrgLSTM as train

#from datetime import datetime, timedelta as dt
#from zoneinfo import ZoneInfo

#import random
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Predict(model, df, scaler, look_back_days, forecast_days=30):

    # --------------------------------------------------
    # 1. DEFINE FEATURES IN THE SAME ORDER AS PREPARE_DATA
    # --------------------------------------------------
    feature_cols = [
        'pct_open',
        'pct_close',
        'pct_high',
        'pct_low',

        'daily_return',
        'log_return',

        'sma_5_ratio',
        'ema_5_ratio',
        'sma_10_ratio',
        'ema_10_ratio',
        'sma_20_ratio',
        'ema_20_ratio',

        'rsi_14',

        'macd',
        'macd_signal',
        'macd_hist',

        'return_lag_1',
        'return_lag_2',
        'return_lag_3',
        'return_lag_5',
        'return_lag_10',
    ]

    if 'volume' in df.columns:
        feature_cols += [
            'volume_pct_change',
            'relative_volume',
            'obv_pct_change',
            'cmf_20',

            'volume_change_lag_1',
            'volume_change_lag_2',
            'volume_change_lag_3',
            'volume_change_lag_5',
            'volume_change_lag_10',
        ]

    # --------------------------------------------------
    # 2. GET THE MOST RECENT LOOKBACK WINDOW
    # --------------------------------------------------
    clean_df = (
        df.replace([np.inf, -np.inf], np.nan)
          .dropna(subset=feature_cols + ['close'])
    )

    if len(clean_df) < look_back_days:
        raise ValueError(
            f"Need at least {look_back_days} valid rows; "
            f"only {len(clean_df)} are available."
        )

    current_window = clean_df[feature_cols].iloc[
        -look_back_days:
    ].to_numpy(dtype=np.float32)

    # Shape: (1, look_back_days, number_of_features)
    latest_window = current_window[np.newaxis, :, :]

    # --------------------------------------------------
    # 3. SCALE FEATURES USING THE TRAINED SCALER
    # --------------------------------------------------
    n_features = latest_window.shape[2]

    latest_window = scaler.transform(
        latest_window.reshape(-1, n_features)
    ).reshape(
        1, look_back_days, n_features
    ).astype(np.float32)

    # --------------------------------------------------
    # 4. PREDICT THE FUTURE/CURRENT PRICE RATIO
    # --------------------------------------------------
    predicted_ratio = float(
        model.predict(latest_window, verbose=0)[0, 0]
    )

    # --------------------------------------------------
    # 5. CONVERT RATIO INTO PERCENTAGE CHANGE AND PRICE
    # --------------------------------------------------
    current_price = float(clean_df['close'].iloc[-1])

    predicted_pct_change = (predicted_ratio - 1.0) * 100.0

    predicted_price = current_price * predicted_ratio

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
    plt.title(f'MultLSTM {ticker} Stock Price Prediction')
    plt.legend()
    plt.show()


def Run_Bot(stock_data_path_base, ticker, tickers, lookback_days=30, forecast_days=30, PLOT=True):
    # Load Training Data
    # If erroring, check imports
    #print("Getting candles...")
    #candles_df = get_data.Get_Candles("AAPL", datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")) - dt(hours=1))
    #print("Creating CSV and plotting...")
    #get_data.Create_Training_CSV(candles_df, "TrainCandles.csv")
    #print("CSV and plot created successfully!\n\n")
    
    # Prepare Data
    stock_data = train.Load_Stock_Data(f'{stock_data_path_base}_{ticker}.csv')
    df = train.Prepare_Data(stock_data, lookback_days, forecast_days)
    
    # Train Model while checking if a saved model exists
    saved_model_exists = True
    metrics = [-1, -1]
    
    try:
        print('A model has already been trained, loading model...')
        model = tf.keras.models.load_model("MachineLearningTrader/LrgLSTM_Model/large_stock_lstm.keras")
        scaler = joblib.load("MachineLearningTrader/LrgLSTM_Model/large_stock_scaler.joblib")
        print('Model loaded successfully!')
    except Exception:
        print("No saved model was found or there was an error loading it, training a new model...")
        saved_model_exists = False


    if not saved_model_exists:
        stock_training_data = train.Load_Stock_Data_Training(stock_data_path_base, tickers)
        x, y, df_total, anchor_prices, target_dates = train.Prepare_Data_Training(stock_training_data, lookback_days, forecast_days)

        model, scaler, metrics = train.Train_Model(df, x, y, anchor_prices, target_dates, lookback_days, forecast_days, PLOT)
    
        model.save("MachineLearningTrader/LrgLSTM_Model/large_stock_lstm.keras")
        joblib.dump(scaler, "MachineLearningTrader/LrgLSTM_Model/large_stock_scaler.joblib")
        
    #model, scaler, metrics = train.Train_Model(df, x, y, anchor_prices, target_dates, lookback_days, forecast_days, PLOT)
    
    
    # Make and Chart Prediction
    predicted_pct_change, future_price = Predict(model, df, scaler, lookback_days, forecast_days)
    
    if PLOT:
        Plot_Predictions(df, future_price, ticker, forecast_days)
    
    print(f'{forecast_days}-Day earnings are {future_price - df['close'].iloc[-1]:.2f} (from a price of {df['close'].iloc[-1]:.2f} to a predicted price of {future_price:.2f}), with a return of {(predicted_pct_change):.2f}%')
    
    return float(predicted_pct_change / 100), float(future_price), float(df['close'].iloc[-1]), metrics


    