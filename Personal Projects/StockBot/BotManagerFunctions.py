###- Import Statements
import pandas as pd

## Model Imports
#from MachineLearningTrader.HistGrad_Model import Main_HistGrad as HistGrad
#from MachineLearningTrader.LogReg_Model import Main_LogReg as LogReg
#from MachineLearningTrader.MultLSTM_Model import Main_MultLSTM as MultLSTM
#from MachineLearningTrader.LrgLSTM_Model import Main_LrgLSTM as LrgLSTM
#from MachineLearningTrader.MultVar_Model import Main_MultVar as MultVar
#from MachineLearningTrader.Pct_Model import Main_Pct as Pct
#from MachineLearningTrader.Raw_Model import Main_Raw as Raw
#from MachineLearningTrader.SglPred_Model import Main_SglPred as SglPred
#from MachineLearningTrader.Video_Model import VersionVideo as Video
#from TraditionalBot import Trad as Trad

# Local Program Imports
from MachineLearningTrader import configML 
from MachineLearningTrader import GetTrainingData as GetData
import AlpacaHelper as alpaca_helper


from pprint import pprint

from datetime import datetime, timedelta as dt
from zoneinfo import ZoneInfo

#import random
###-



###- Functions
def Save_Stocks_Dictionary(dictionary, file_name):
    rows = []

    for ticker, models in dictionary.items():
        for model, metrics in models.items():
            row = {
                "stock_ticker": ticker,
                "model": model,
                **metrics
            }
            rows.append(row)
        
    df = pd.DataFrame(rows)

    df.to_csv(file_name, index=False)

def Save_Trad_Dictionary(dictionary, file_name):
    rows = []
    
    for ticker, metrics in dictionary.items():
        row = {
            "ticker": ticker,
            **metrics
            #"entry_price": dictionary[ticker]["Entry_Price"],
            #"stop_loss": dictionary[ticker]["Stop_Loss"],
            #"take_profit": dictionary[ticker]["Take_Profit"],
            #"return_percent": dictionary[ticker]["Return_Percent"],
            }
        rows.append(row)
        
    df = pd.DataFrame(rows)
    
    df.to_csv(file_name, index=False)

def Save_Rankings_Dictionary(dictionary, file_name):
    rows = []

    for model, metrics in dictionary.items():
        row = {
            "model": model,
            **metrics
        }
        rows.append(row)

    df = pd.DataFrame(rows)

    df.to_csv(file_name, index=False)

def Load_Stocks_Dictionary(file_name):
    dictionary = {}
    df = pd.read_csv(file_name)

    for _, row in df.iterrows():
        ticker = row["stock_ticker"]
        model = row["model"]
        
        metrics = row.drop(["stock_ticker", "model"]).dropna().to_dict()
        
        dictionary.setdefault(ticker, {})[model] = metrics
        
    return dictionary

def Load_Trad_Dictionary(file_name):
    df = pd.read_csv(file_name)

    dictionary = {}

    for _, row in df.iterrows():
        ticker = row["ticker"]

        metrics = row.drop("ticker").to_dict()

        dictionary[ticker] = metrics

    return dictionary

def Load_Rankings_Dictionary(file_name):
    df = pd.read_csv(file_name)

    dictionary = {}

    for _, row in df.iterrows():
        ticker = row["ticker"]

        metrics = row.drop("model").to_dict()

        dictionary[ticker] = metrics

    return dictionary



# data_path generally = 'TrainCandles/TrainCandles_'
# tickers generally = configML.CONST_STOCK_SYMBOLS
# These CSVs are saved locally into the data path, so nothing is returned
def CreateDataCSVs(data_path, tickers):
    for ticker in tickers:
        data_path = f'{data_path}_{ticker}.csv'
        
        # Load data for current ticker
        candles_retrieved = False
        times_attempted = 1
        print(f"\nGetting candles for {ticker} on attempt {times_attempted}...")
        while not candles_retrieved:
            try:
                candles_df = GetData.Get_Candles(ticker, datetime(2020, 1, 1), datetime.now(ZoneInfo("America/New_York")) - dt(hours=1))
                candles_retrieved = True
            except:
                times_attempted += 1
            
        
        print("Creating CSV...")
        GetData.Create_Training_CSV(candles_df, f'TrainCandles/TrainCandles_{ticker}.csv')
        print("CSV created successfully!\n\n")
    
    
    
# data_path generally = 'TrainCandles/TrainCandles'
# tickers generally = configML.CONST_STOCK_SYMBOLS
# models generally = configML.CONST_MODEL_TYPES
# This returns 4 dictionaries; the model predictions, the traditional model predictions, and then the top 10 of each respectively
def MakePredictions(data_path, tickers, models, LOOKBACK_DAYS=60, FORECAST_DAYS=15, STOCKS_TO_PURCHASE=10, PLOT=False):
    Dict_Stock_Predictions = {}
    Dict_Trad_Stocks = {}
    
    for ticker in configML.CONST_STOCK_SYMBOLS:    
        print(f'---Starting Predictions on Ticker {ticker}---')
           
        data_path_ticker = f'{data_path}_{ticker}.csv'
        
        # Run each model on current dataset and save predictions in dictionary
        for model in models:
            model_name = model.__name__   
            model_name = model_name.split('.')[-1]
            
            print(f'\nStarting Model {model_name}...')
            
            # Handle Run_Bot() Functionality of Models
            try:
                if model_name == 'Main_LogReg':
                    pred_price = 0
                    pct, curr_price, metrics = model.Run_Bot(data_path_ticker, FORECAST_DAYS)
                elif model_name == 'VersionVideo':
                    pct, pred_price, curr_price, metrics = model.Run_Bot(data_path_ticker, ticker, FORECAST_DAYS, PLOT)
                elif model_name == 'Main_LrgLSTM':
                    pct, pred_price, curr_price, metrics = model.Run_Bot(data_path, ticker, tickers, LOOKBACK_DAYS, FORECAST_DAYS, PLOT)
                elif model_name == 'Trad':
                    # Handle Traditional Bot
                    print('Starting Traditional Model...')
                    entry_price, stop_loss, take_profit, return_percent = model.RunBot(data_path_ticker, ticker, LOOKBACK_DAYS)
                    Dict_Trad_Stocks[ticker] = {
                        'Entry_Price': round(entry_price, 2),
                        'Stop_Loss': round(stop_loss, 2),
                        'Take_Profit': round(take_profit, 2),
                        'Return_Percent': round(return_percent, 2)
                        }
                else:
                    pct, pred_price, curr_price, metrics = model.Run_Bot(data_path_ticker, ticker, LOOKBACK_DAYS, FORECAST_DAYS, PLOT)
            except Exception as e:
                print(f'An error has occurred when running {model_name}.  The error is {e}')
                pct = 0
                pred_price = 0
                curr_price = 1000000
                metrics = [0,0]
            
            Dict_Stock_Predictions.setdefault(model_name, {})[ticker] = {
                'Predicted_Returns': round(pct, 3),
                'Predicted_Price': round(pred_price, 3),
                'Current_Price': round(curr_price, 3),
                'xMSE': round(metrics[0], 2),
                'xR2': round(metrics[1], 4)
            }
            
        
    # Print dictionary and get top 10 stocks from list for each model based on returns
    print('\nData Collection and Predictions Complete!\n')
    #pprint(Dict_Stock_Predictions)
    
    Dict_Top_Stock_Predictions = {}
    for model, stocks in Dict_Stock_Predictions.items():
        Dict_Top_Stock_Predictions[model] = dict(
            sorted(
                stocks.items(),
                key=lambda x: x[1]["Predicted_Returns"],
                reverse=True
            )[:STOCKS_TO_PURCHASE]
        )
        
        
    Dict_Top_Trad_Stocks = dict(
        sorted(
            Dict_Trad_Stocks.items(),
            key=lambda x: x[1]["Return_Percent"],
            reverse=True
        )[:STOCKS_TO_PURCHASE])
    
    print('\nDictionaries Sorted!')
    
    return Dict_Stock_Predictions, Dict_Trad_Stocks, Dict_Top_Stock_Predictions, Dict_Top_Trad_Stocks



# tickers generally = configML.CONST_STOCK_SYMBOLS
# models generally = configML.CONST_MODEL_TYPES
# Dict_Stock_Predictions will either be loaded from a previous date or returned from MakePredictions
# Dict_Top_Stock_Predictions will either be loaded from a previous date or returned from MakePredictions
# Dict_Top_Trad_Stocks will either be loaded from a previous date or returned from MakePredictions 
# This returns the Dictionary of the model rankings and the failed buy dictionary for manual error handling
def CompleteBuyRequests(tickers, models, Dict_Stock_Predictions, Dict_Top_Stock_Predictions, Dict_Top_Trad_Stocks, STOCKS_TO_PURCHASE=10):
    # Make a dictionary that catches any failed BUY or SELL requests to be manually completed later
    Dict_Failed_Requests = {}
    
    for model in models:
        model_name = model.__name__   
        model_name = model_name.split('.')[-1]
        
        if model_name == 'Trad':
            # Complete the buy orders for the traditional bot 
            # These do not require a sell order since they will auto sell when they reach a specific price  
            trading_client = alpaca_helper.GetTradingClient(configML.CONST_ALPACA_KEY_Trad, configML.CONST_ALPACA_SECRET_Trad)
            
            # Add the model name and its total account value to the model list
            total_equity, total_cash = alpaca_helper.GetAccountValue(trading_client)
            
            print(f'\nFor trad model; Total equity is: {total_equity}, total cash is: {total_cash}')
            for ticker in Dict_Top_Trad_Stocks:
                if Dict_Top_Trad_Stocks[ticker]['Entry_Price'] != 0:
                    quantity = round((total_cash * (0.75/STOCKS_TO_PURCHASE)) / Dict_Top_Trad_Stocks[ticker]['Entry_Price'], 0)
                    
                    print(f'Buying {quantity} shares of {ticker} for traditional model')
                    try:
                        alpaca_helper.Buy_Stock_Traditional(trading_client, ticker, Dict_Top_Trad_Stocks[ticker]['Stop_Loss'], Dict_Top_Trad_Stocks[ticker]['Take_Profit'], quantity)
                    except Exception as e:
                        print(f'Purchasing {quantity} shares of {ticker} failed for Trad for reason {e}')
                        Dict_Failed_Requests.setdefault('Trad', {})[ticker] = {
                            'Predicted_Returns': round(Dict_Top_Trad_Stocks[ticker]['Predicted_Returns'], 3),
                            'Predicted_Price': round(Dict_Top_Trad_Stocks[ticker]['Predicted_Price'], 3),
                            'Current_Price': round(Dict_Top_Trad_Stocks[ticker]['Current_Price'], 3),
                            'xMSE': round(Dict_Top_Trad_Stocks[ticker]['xMSE'], 2),
                            'xR2': round(Dict_Top_Trad_Stocks[ticker]['xR2'], 4),
                            'Buy_Sell': 'BUY',
                            'Exception': str(e)
                        }
        else:
            # Make a trading client
            trading_client = alpaca_helper.GetTradingClient(getattr(configML, f'CONST_ALPACA_KEY_{model_name}'), getattr(configML, f'CONST_ALPACA_SECRET_{model_name}'))
            
            # Add the model name and its total account value to the model list
            total_equity, total_cash = alpaca_helper.GetAccountValue(trading_client)
            
            print(f'\nFor model {model_name}; Total equity is: {total_equity}, total cash is: {total_cash}')
            

                
            # Complete the BUY order requests for all non trad models
            for ticker in Dict_Top_Stock_Predictions[model_name]:
                current_price = Dict_Top_Stock_Predictions[model_name][ticker]['Current_Price']
                quantity = round((total_cash * (0.75/STOCKS_TO_PURCHASE)) / current_price, 2)
                            
                # Buy the stock ticker at set percentage of the cash
                print(f'Buying {quantity:.2f} shares of {ticker} for model {model_name}')
                try:
                    alpaca_helper.BuyStock(trading_client, ticker, quantity)
                except Exception as e:
                    print(f'Purchasing {quantity} shares of {ticker} failed for {model_name} for reason {e}')
                    Dict_Failed_Requests.setdefault(model_name, {})[ticker] = {
                        'Predicted_Returns': round(Dict_Top_Stock_Predictions[model_name][ticker]['Predicted_Returns'], 3),
                        'Predicted_Price': round(Dict_Top_Stock_Predictions[model_name][ticker]['Predicted_Price'], 3),
                        'Current_Price': round(Dict_Top_Stock_Predictions[model_name][ticker]['Current_Price'], 3),
                        'xMSE': round(Dict_Top_Stock_Predictions[model_name][ticker]['xMSE'], 2),
                        'xR2': round(Dict_Top_Stock_Predictions[model_name][ticker]['xR2'], 4),
                        'Buy_Sell': 'BUY',
                        'Exception': str(e)
                    }
                                    
    return Dict_Failed_Requests



# tickers generally = configML.CONST_STOCK_SYMBOLS
# models generally = configML.CONST_MODEL_TYPES
# Dict_Stock_Predictions will either be loaded from a previous date or returned from MakePredictions
# This returns the Dictionary of the model rankings and the failed buy/sell dictionary for manual error handling
def CompleteSellRequests(tickers, models, Dict_Stock_Predictions):
    # Make a dictionary that catches any failed BUY or SELL requests to be manually completed later
    Dict_Failed_Requests = {}
    
    for model in models:
        model_name = model.__name__   
        model_name = model_name.split('.')[-1]
        
        # Trad auto sells at certain pre-set prices so it is not necessary to sell for it
        if model_name == 'Trad':
            continue
        
        # Make a trading client
        trading_client = alpaca_helper.GetTradingClient(getattr(configML, f'CONST_ALPACA_KEY_{model_name}'), getattr(configML, f'CONST_ALPACA_SECRET_{model_name}'))
        
        # Complete the SELL order requests
        Dict_Current_Positions = alpaca_helper.GetCurrentPositions(trading_client)
        
        for ticker in Dict_Current_Positions:
            curr_pct_change = float(Dict_Current_Positions[ticker]['Current_Price']) / float(Dict_Current_Positions[ticker]['Average_Entry_Price'])
            
            # If the current gains are greater than the next predicted gains or lower than 2% loss, then sell the stock
            if curr_pct_change > Dict_Stock_Predictions[model_name][ticker]['Predicted_Returns'] or curr_pct_change < 0.98:
                print(f'Selling {(float(Dict_Current_Positions[ticker]['Quantity'])):.2f} shares of {ticker} for model {model_name}')
                
                try:
                    alpaca_helper.SellStock(trading_client, ticker, float(Dict_Current_Positions[ticker]['Quantity']))
                except Exception as e:
                    print(f'Purchasing {Dict_Current_Positions[ticker]['Quantity']} shares of {ticker} failed for {model_name} for reason {e}')
                    Dict_Failed_Requests.setdefault(model_name, {})[ticker] = {
                        'Predicted_Returns': round(Dict_Current_Positions[ticker]['Predicted_Returns'], 3),
                        'Predicted_Price': round(Dict_Current_Positions[ticker]['Predicted_Price'], 3),
                        'Current_Price': round(Dict_Current_Positions[ticker]['Current_Price'], 3),
                        'xMSE': round(Dict_Current_Positions[ticker]['xMSE'], 2),
                        'xR2': round(Dict_Current_Positions[ticker]['xR2'], 4),
                        'Buy_Sell': 'SELL',
                        'Exception': str(e)
                }

    return Dict_Failed_Requests

            
# models generally = configML.CONST_MODEL_TYPES
# This will return a dictionary of the model rankings to be saved
def RankModels(models):
    Dict_Ranked_Models = {}

    for model in models:
        model_name = model.__name__   
        model_name = model_name.split('.')[-1]
        
        # Make a trading client
        trading_client = alpaca_helper.GetTradingClient(getattr(configML, f'CONST_ALPACA_KEY_{model_name}'), getattr(configML, f'CONST_ALPACA_SECRET_{model_name}'))
        
        # Add the model name and its total account value to the model list
        total_equity, total_cash = alpaca_helper.GetAccountValue(trading_client)
        Dict_Ranked_Models[model_name] = {
            'Total_Equity': total_equity,
            'Total_Cash': total_cash
        }

        
        print(f'\nFor model {model_name}; Total equity is: {total_equity}, total cash is: {total_cash}')

    # Rank the models based on the total equity    
    ranked_models = sorted(
        Dict_Ranked_Models.items(),
        key=lambda item: float(item[1]['Total_Equity']),
        reverse=True
    )
    
    # Print current model rankings
    print('The current standings of the models are: ')
    pprint(ranked_models)

    return Dict_Ranked_Models    

###-





