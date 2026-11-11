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

def Prepare_Data(df, lookback_days=30):
    print('Preparing data...')
    df = df[['close']].copy()
    df['prediction'] = df[['close']].shift(-lookback_days)
    
    x = np.array(df.drop(['prediction'], axis=1))[:-lookback_days] #features
    y = np.array(df['prediction'])[:-lookback_days] #target array

    return x, y, df

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

