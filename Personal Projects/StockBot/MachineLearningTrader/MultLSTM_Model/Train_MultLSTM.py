###- Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Sklearn Imports
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
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



def Prepare_Data(df, look_back_days = 30, forecast_days=30):
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
    anchor_prices = []
    target_dates = []

    # Each sample uses the previous look_back_days rows.
    # Predict the ratio of the future close to the current close.
    for i in range(look_back_days, len(df) - look_back_days):

        features = df[feature_cols].iloc[
            i - look_back_days:i
        ].to_numpy(dtype=np.float32)

        x_list.append(features)

        # Future close / close at prediction origin
        target = (
            df['close'].iloc[i + forecast_days]
            / df['close'].iloc[i]
        )

        y_list.append(target)

        # Keep the starting price so ratios can be converted
        # back into predicted prices during evaluation.
        anchor_prices.append(df['close'].iloc[i])

        # Date of the actual future target
        target_dates.append(df.index[i + forecast_days])

    n_features = len(feature_cols)

    x = np.asarray(x_list, dtype=np.float32).reshape(
        -1, look_back_days, n_features
    )

    y = np.asarray(y_list, dtype=np.float32)
    anchor_prices = np.asarray(anchor_prices, dtype=np.float32)
    target_dates = np.asarray(target_dates)

    print(f'Features per day: {n_features}')
    print(f'Lookback days: {look_back_days}')
    print(f'LSTM input shape: {x.shape}')
    print(f'Training samples: {len(x)}')

    return x, y, df1, anchor_prices, target_dates



#******************************************************************************************************************



def Train_Model(df, x, y, anchor_prices, target_dates, look_back_days=30, forecast_days=30, PLOT=True):
    BATCH_SIZE = 32
    EPOCHS = 100

    # --------------------------------------------------
    # 1. TEMPORAL TRAIN / VALIDATION / TEST SPLIT
    # --------------------------------------------------
    n = len(x)
    train_end = int(n * 0.70)
    val_end = int(n * 0.85)

    x_train = x[:train_end]
    x_val = x[train_end:val_end]
    x_test = x[val_end:]

    y_train = y[:train_end]
    y_val = y[train_end:val_end]
    y_test = y[val_end:]

    anchor_test = anchor_prices[val_end:]
    dates_test = target_dates[val_end:]

    # --------------------------------------------------
    # 2. SCALE INPUT FEATURES ONLY
    # --------------------------------------------------
    n_features = x.shape[2]

    scaler = MinMaxScaler(feature_range=(0, 1))

    # Fit only on training data. Flatten temporarily for
    # the scaler, then restore the LSTM sequence shape.
    x_train_2d = x_train.reshape(-1, n_features)
    scaler.fit(x_train_2d)

    x_train = scale_sequences(x_train, n_features, scaler)
    x_val = scale_sequences(x_val, n_features, scaler)
    x_test = scale_sequences(x_test, n_features, scaler)

    # y remains the unscaled future/current price ratio.
    y_train = y_train.astype(np.float32)
    y_val = y_val.astype(np.float32)
    y_test = y_test.astype(np.float32)

    print("Training samples:", len(x_train))
    print("Validation samples:", len(x_val))
    print("Testing samples:", len(x_test))
    print("Input shape:", x_train.shape)
    print("Target shape:", y_train.shape)

    # --------------------------------------------------
    # 3. BUILD LSTM
    # --------------------------------------------------
    print("Training model...")

    model = tf.keras.Sequential([
        tf.keras.layers.Input(
            shape=(look_back_days, n_features)
        ),
        tf.keras.layers.LSTM(
            units=64,
            return_sequences=False
        ),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=0.001
        ),
        loss="mean_squared_error",
        metrics=["mean_absolute_error"]
    )

    model.summary()

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=10,
            restore_best_weights=True
        )
    ]

    history = model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        shuffle=False,
        callbacks=callbacks,
        verbose=1
    )

    # --------------------------------------------------
    # 4. PLOT TRAINING HISTORY
    # --------------------------------------------------
    if PLOT:
        plt.figure(figsize=(10, 5))
        plt.plot(history.history["loss"], label="Training loss")
        plt.plot(
            history.history["val_loss"],
            label="Validation loss"
            )
        plt.xlabel("Epoch")
        plt.ylabel("Mean squared error (price ratio)")
        plt.title("Stock LSTM training")
        plt.legend()
        plt.tight_layout()
        plt.show()

    # --------------------------------------------------
    # 5. PREDICT AND CONVERT RATIOS TO PRICES
    # --------------------------------------------------
    print("Model trained. Evaluating performance...")

    pred_ratio = model.predict(x_test, verbose=0).ravel()

    # The target is future_close / starting_close to give a usable return percent
    lstm_prices = pred_ratio * anchor_test
    y_test_prices = y_test * anchor_test

    # Naive forecast: assume the price does not change.
    baseline_prices = anchor_test.copy()

    # --------------------------------------------------
    # 6. EVALUATE
    # --------------------------------------------------
    mse = mean_squared_error(y_test_prices, lstm_prices)
    r2 = r2_score(y_test_prices, lstm_prices)

    lstm_metrics = evaluate_predictions(
        y_test_prices, lstm_prices
    )
    baseline_metrics = evaluate_predictions(
        y_test_prices, baseline_prices
    )

    if PLOT:
        plt.figure(figsize=(12, 6))
        
        plt.plot(
            dates_test,
            y_test_prices,
            label="Actual price",
            color="black"
            )
        plt.plot(
            dates_test,
            lstm_prices,
            label="LSTM prediction",
            alpha=0.8
            )
        plt.plot(
            dates_test,
            baseline_prices,
            label="Naive baseline",
            alpha=0.7
            )
        
        plt.title(
            f"Stock {forecast_days}-trading-day-ahead predictions"
            )
        plt.xlabel("Target date")
        plt.ylabel("Closing price ($)")
        plt.legend()
        plt.tight_layout()
        plt.show()

    print("LSTM:", lstm_metrics)
    print("Naive baseline:", baseline_metrics)
    print("Model Evaluation:")
    print(f"MSE: {mse:.4f}")
    print(f"R2: {r2:.4f}")

    metrics = [mse, r2]    

    return model, scaler, metrics


def scale_sequences(data, n_features, scaler):
    original_shape = data.shape
    transformed = scaler.transform(data.reshape(-1, n_features))
    
    return transformed.reshape(original_shape).astype(np.float32)


def evaluate_predictions(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    return {
        "MAE": mae,
        "RMSE": rmse
    }