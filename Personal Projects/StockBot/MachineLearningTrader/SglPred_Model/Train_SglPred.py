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

def Prepare_Data(df, lookback_days=30, forecast_days=30):
    print('Preparing data...')
    
    df['pct_open'] = df['open'].pct_change()
    df['pct_close'] = df['close'].pct_change()    
    df['pct_high'] = df['high'].pct_change()
    df['pct_low'] = df['low'].pct_change()

    df1 = df.copy()
    
    df = df.dropna().reset_index(drop=True)
    
    x_list = []
    y_list = []
    
    for i in range(lookback_days, len(df) - lookback_days):
        # Four features, each containing the previous 30 days
        features = np.column_stack([
            df['pct_open'].iloc[i-lookback_days:i].values,
            df['pct_close'].iloc[i-lookback_days:i].values,
            df['pct_high'].iloc[i-lookback_days:i].values,
            df['pct_low'].iloc[i-lookback_days:i].values
        ])

        x_list.append(features)

        # Target: closing price percentage change 30 days ahead
        y_list.append(df['close'].iloc[i + forecast_days] / df['close'].iloc[i])
    
    x = np.array(x_list)
    y = np.array(y_list)

    x = x[lookback_days:]
    y = y[lookback_days:]

    x = x.reshape(x.shape[0], -1)
    
    return x, y, df1

def Train_Model(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
    
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
