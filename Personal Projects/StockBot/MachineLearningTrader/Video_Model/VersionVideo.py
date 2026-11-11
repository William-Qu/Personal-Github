# -*- coding: utf-8 -*-
# LAST TIMESTAMP ON TUTORIAL: 12.14
    
'''TODO!!!
    -Save the model
    -Add a way for the model to buy and sell stocks
    -Look into different modelm types outside of linear regression
    -Add more features for the model to be trained on
        -moving averages, rsi, macD, daily returns, volume based indicators, lag features
    -See if it works to train on multiple stocks for a general stock MLbot
        -I suspect this is the best way for it to predict prices
    
'''
    
# Alpacas Login:
    # Username: 789william@hotmail.ca
    # Password: CompEngSideProject1!

###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sklearn Imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
###-

###- Initializations
plt.style.use('fivethirtyeight')
###-

def Load_Stock_Data(csv_file):
    print('Loading data...')
    df = pd.read_csv(csv_file)
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    return df

def Prepare_Data(df, forecast_days=30):
    print('Preparing data...')
    df = df[['close']].copy()
    df['prediction'] = df[['close']].shift(-forecast_days)
    
    x = np.array(df.drop(['prediction'], axis=1))[:-forecast_days] #features
    y = np.array(df['prediction'])[:-forecast_days] #target array

    return x, y, df

def Train_Model(x, y, forecast_days=30):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=33)
    
    # Training on the x_train to get the data on y_train
    print('Training model...')
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    # It will now try to match y_test using the x_test (I think the different times)
    print('Model trained.  Evaluating performance...')
    predictions = model.predict(x_test)
    
    # This will give us our error value (we want low but not 0)
    mse = mean_squared_error(y_test, predictions)
    
    # Measures how much of the variation in the target variable your model can explain
    r2 = r2_score(y_test, predictions)
    
    print('Model Evaluation:')
    print(f'MSE: {mse:.2f}')
    print(f'R2: {r2:.4f}')
    
    metrics = [mse, r2]

    return model, metrics

def Predict(model, df, forecast_days=30):
    x_future = np.array(df.drop(['prediction'], axis=1))[-forecast_days:]
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
    plt.title(f'Video {ticker} Stock Price Prediction')
    plt.legend()
    plt.show()
    
    
def Run_Bot(stock_data_path, ticker, forecast_days=30, PLOT=True):
    stock_data = Load_Stock_Data(stock_data_path)
    
    x, y, df = Prepare_Data(stock_data, forecast_days)
    model, metrics = Train_Model(x, y, forecast_days)
    future_predictions = Predict(model, df, forecast_days)
    
    if PLOT:
        Plot_Predictions(df, future_predictions, ticker, forecast_days)
    
    print('Future Price Predictions')
    print(future_predictions)
    
    print(f'{forecast_days}-Day earnings are {future_predictions[-1] - df['close'].iloc[-1]:.2f} (predicted price of {future_predictions[-1]:.2f}), with a return of {((future_predictions[-1] / df['close'].iloc[-1]) - 1) * 100:.2f}%')
    
    return float((future_predictions[-1] / df['close'].iloc[-1]) - 1), float(future_predictions[-1]), float(df['close'].iloc[-1]), metrics