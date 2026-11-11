###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sklearn Imports
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import HistGradientBoostingRegressor
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


#********************************************************************************************************************



def Prepare_Data(df, lookback_days=30, forecast_days=30):
    print('Preparing data...')

    # --------------------------------------------------
    # 1. DAILY RETURNS / PRICE CHANGES
    # --------------------------------------------------
    df['pct_open'] = df['open'].pct_change()
    df['pct_close'] = df['close'].pct_change()
    df['pct_high'] = df['high'].pct_change()
    df['pct_low'] = df['low'].pct_change()

    df['daily_return'] = df['close'].pct_change()
    
    # Log returns
    df['log_return'] = np.log(
        df['close'] / df['close'].shift(1)
    )

    # --------------------------------------------------
    # 2. MOVING AVERAGES
    # --------------------------------------------------
    ma_periods = [5, 10, 20]

    for period in ma_periods:
        # Simple Moving Average
        sma = df['close'].rolling(window=period).mean()

        # Exponential Moving Average
        ema = df['close'].ewm(
            span=period, adjust=False
        ).mean()

        # Normalize relative to price
        df[f'sma_{period}_ratio'] = df['close'] / sma - 1
        df[f'ema_{period}_ratio'] = df['close'] / ema - 1

    # --------------------------------------------------
    # 3. RSI (14-DAY RELATIVE STRENGTH INDEX)
    # --------------------------------------------------
    delta = df['close'].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(
        alpha=1/14, min_periods=14, adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1/14, min_periods=14, adjust=False
    ).mean()

    rs = avg_gain / avg_loss

    df['rsi_14'] = 100 - (100 / (1 + rs))

    # Handle edge cases
    df.loc[
        (avg_loss == 0) & (avg_gain > 0), 'rsi_14'
    ] = 100

    df.loc[
        (avg_loss == 0) & (avg_gain == 0), 'rsi_14'
    ] = 50

    # --------------------------------------------------
    # 4. MACD (12, 26, 9)
    # --------------------------------------------------
    ema_12 = df['close'].ewm(
        span=12, adjust=False
    ).mean()

    ema_26 = df['close'].ewm(
        span=26, adjust=False
    ).mean()

    macd = ema_12 - ema_26

    macd_signal = macd.ewm(
        span=9, adjust=False
    ).mean()

    # Normalize MACD to make it comparable across prices
    df['macd'] = macd / df['close']
    df['macd_signal'] = macd_signal / df['close']
    df['macd_hist'] = (macd - macd_signal) / df['close']

    # --------------------------------------------------
    # 5. VOLUME INDICATORS
    # --------------------------------------------------
    if 'volume' in df.columns:

        # Daily volume percentage change
        df['volume_pct_change'] = df['volume'].pct_change()

        # Relative volume compared with the previous
        # 20-day average (shifted to exclude today's volume)
        volume_avg_20 = df['volume'].rolling(
            window=20
        ).mean().shift(1)

        df['relative_volume'] = (
            df['volume'] / volume_avg_20
        )

        # On-Balance Volume (OBV)
        direction = np.sign(df['close'].diff()).fillna(0)

        df['obv'] = (
            direction * df['volume']
        ).cumsum()

        # Normalize OBV changes to reduce scale issues
        df['obv_pct_change'] = df['obv'].pct_change()

        # Chaikin Money Flow (20-day CMF)
        price_range = df['high'] - df['low']

        money_flow_multiplier = (
            (df['close'] - df['low'])
            - (df['high'] - df['close'])
        ) / price_range.replace(0, np.nan)

        money_flow_volume = (
            money_flow_multiplier * df['volume']
        )

        volume_sum = df['volume'].rolling(20).sum()

        df['cmf_20'] = (
            money_flow_volume.rolling(20).sum()
            / volume_sum.replace(0, np.nan)
        )

    # --------------------------------------------------
    # 6. LAG FEATURES
    # --------------------------------------------------
    lag_periods = [1, 2, 3, 5, 10]

    for lag in lag_periods:

        # Past daily returns
        df[f'return_lag_{lag}'] = (
            df['daily_return'].shift(lag)
        )

        # Past volume changes
        if 'volume' in df.columns:
            df[f'volume_change_lag_{lag}'] = (
                df['volume_pct_change'].shift(lag)
            )

    # --------------------------------------------------
    # 7. DEFINE FEATURES AND TARGET
    # --------------------------------------------------
    feature_cols = [
        # Original price changes
        'pct_open',
        'pct_close',
        'pct_high',
        'pct_low',

        # Returns
        'daily_return',
        'log_return',

        # Moving averages
        *[
            f'{ma_type}_{period}_ratio'
            for period in ma_periods
            for ma_type in ['sma', 'ema']
        ],

        # RSI
        'rsi_14',

        # MACD
        'macd',
        'macd_signal',
        'macd_hist',

        # Return lags
        *[
            f'return_lag_{lag}'
            for lag in lag_periods
        ],
    ]

    if 'volume' in df.columns:
        feature_cols += [
            'volume_pct_change',
            'relative_volume',
            'obv_pct_change',
            'cmf_20',
        ]

        feature_cols += [
            f'volume_change_lag_{lag}'
            for lag in lag_periods
        ]
            
    # Replace infinite values and remove incomplete rows
    df = df.replace([np.inf, -np.inf], np.nan)

    # Preserve the enriched DataFrame for downstream use
    df1 = df.copy()

    # Drop rows without valid features or targets
    df = df.dropna(
        subset=feature_cols + ['close']
    ).reset_index(drop=True)

    x_list = []
    y_list = []

    # Each sample uses the previous lookback_days rows
    # Target is the closing-price ratio forecast_days ahead
    for i in range(lookback_days, len(df) - lookback_days):

        features = df[feature_cols].iloc[
            i - lookback_days:i
        ].to_numpy(dtype=float)

        x_list.append(features)

        target = (
            df['close'].iloc[i + forecast_days]
            / df['close'].iloc[i]
        )

        y_list.append(target)

    x = np.asarray(x_list, dtype=float)
    y = np.asarray(y_list, dtype=float)

    # Flatten: lookback days × features -> 2D matrix
    if len(x) > 0:
        x = x.reshape(x.shape[0], -1)
    else:
        x = np.empty(
            (0, lookback_days * len(feature_cols))
        )

    print(f'Features per day: {len(feature_cols)}')
    print(f'Lookback days: {lookback_days}')
    print(f'Total model inputs: {x.shape[1]}')
    print(f'Training samples: {len(x)}')
    #print(feature_cols)

    return x, y, df1



#******************************************************************************************************************



def Train_Model(x, y, lookback_days):
    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=33, shuffle=False)
    
    
    # Five chronological folds, with a 30-row gap before each test fold.
    #splits = 5 # Original Splits
    cv = TimeSeriesSplit(n_splits=10, gap=lookback_days)
    
    for fold, (train_idx, test_idx) in enumerate(cv.split(x), start=1):
        x_train, x_test = x[train_idx], x[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
    
        print(
            f"Fold {fold}: "
            f"train through row {train_idx[-1]}, "
            f"test from row {test_idx[0]}"
        )
    
    
    
    # Training on the x_train to get the data on y_train
    print('Training model...')
    
    ## Original Hyperparameters
    #model = HistGradientBoostingRegressor(
    #    loss="squared_error",
    #    learning_rate=0.03,
    #    max_iter=200,
    #    max_leaf_nodes=15,
    #    max_depth=4,
    #    min_samples_leaf=50,
    #    l2_regularization=1.0,
    #    early_stopping=False,
    #    random_state=42,
    #)
    
    model = HistGradientBoostingRegressor(
        loss="squared_error",
        learning_rate=0.03,
        max_iter=300,
        max_leaf_nodes=15,
        max_depth=6,
        min_samples_leaf=50,
        l2_regularization=1.0,
        early_stopping=False
    )
    
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
