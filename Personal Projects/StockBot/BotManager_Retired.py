# -*- coding: utf-8 -*-
#x##!!!TODO: Remove the GetTrainingData code from each Machine Learning Bot
#x##!!!TODO: Add a main loop to each bot for easy calling from this manager
#x##!!!TODO: Modify the Traditional Bot to return an output so its stocks can be ranked
#x##!!!TODO: Build buy and sell functionality in this manager
#x##!!!TODO: Build a current stock check function in this manager
#x##!!!TODO: Create readme documentation 
#x##!!!TODO: Figure out how to easily import all training data (maybe don't use as old or can save lin reg models)
#x##!!!TODO: Figure out how to have multiple accounts on alpacas
#x##!!!TODO: Add current price of stock for partitioning current cash purposes (alpacas does have partial buys)

#x##!!!TODO: Fix save rankings dictionary

#x##!!!TODO: Add error prevention dictionary incase a buy or sell fails
#x##!!!TODO: Add a starting symbol x/x to better keep track progress

# Game plan of things to complete:
#x##!!! Create dictionary
#           -Dim(Models * (Stocks * Metrics)
#           -Metics are current price, predicted price, return %
#x##!!! Load Stock data for different stocks
#x##!!! Run models and populate dictionary (Return predictions and metrics)
#x##!!! Determine whether any stocks should be sold; Currently will be sold if current percent change is higher than predicted percent or if it is a ~2% loss
#x##!!! Determine best stocks to buy
#x##!!! Buy sell functionality
#x##!!! Save dictionary to system for future reference
#x##!!! Print results/operations
#x##!!! Print standings between models


# Next steps of things to do after phase 1:

###!!! Add deep learning model
###!!! Add sentiment analysis model with web scraping
###!!! Create a UI for the manager
###!!! Add a system to see if a buy should be made when the program is run instead of just having to hope you are runnign the program on the correct dates
###!!! Increase speed 
#           -Maybe keep all dictionaries downloaded and just update them?
#           -Maybe save LSTM model so it only needs to be trained once ** NEED TO LOOK INTO THIS
###!!! Add randotron model?? (cat-yarn model)

###-


###- Import Statements
import pandas as pd

# Model Imports
from MachineLearningTrader.HistGrad_Model import Main_HistGrad as HistGrad
from MachineLearningTrader.LogReg_Model import Main_LogReg as LogReg
from MachineLearningTrader.MultLSTM_Model import Main_MultLSTM as MultLSTM
from MachineLearningTrader.LrgLSTM_Model import Main_LrgLSTM as LrgLSTM
from MachineLearningTrader.MultVar_Model import Main_MultVar as MultVar
from MachineLearningTrader.Pct_Model import Main_Pct as Pct
from MachineLearningTrader.Raw_Model import Main_Raw as Raw
from MachineLearningTrader.SglPred_Model import Main_SglPred as SglPred
from MachineLearningTrader.Video_Model import VersionVideo as Video
from TraditionalBot import Trad as Trad

# Local Program Imports
from MachineLearningTrader import configML 
from MachineLearningTrader import GetTrainingData as GetData
import AlpacaHelper as alpaca_helper


from pprint import pprint

from datetime import datetime, timedelta as dt
from zoneinfo import ZoneInfo

#import random
###-

###- Constants
models = [HistGrad, MultLSTM, LrgLSTM, MultVar, Pct, Raw, SglPred, LogReg, Video]
###- 



###- Helper Functions
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
    
def Save_Rankings_Dictionary(dictionary, file_name):
    rows = []
    
    for model, equity in dictionary:
        row = {
            "model": model,
            "total_equity": equity
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
###- 


###!!!###- Main Loop -###!!!###
# Initialize Variables
print('-------------------------Starting BotManager-------------------------')
print(datetime.now())
Dict_Stock_Predictions = {}
Dict_Trad_Stocks = {}
STOCKS_TO_PURCHASE = 10
LOOKBACK_DAYS = 60
FORECAST_DAYS = 15
PLOT = False

#Train and Run all models and populate predictions into the dictionary
print('\n-------------------------Phase 1: Pulling Data and Predicting-------------------------')
for ticker in configML.CONST_STOCK_SYMBOLS:
    data_path = f'TrainCandles/TrainCandles_{ticker}.csv'
    
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
    
    # Handle Traditional Bot
    print('Starting Traditional Model...')
    entry_price, stop_loss, take_profit, return_percent = Trad.RunBot(data_path, ticker, LOOKBACK_DAYS)
    Dict_Trad_Stocks[ticker] = {
        'Entry_Price': round(entry_price, 2),
        'Stop_Loss': round(stop_loss, 2),
        'Take_Profit': round(take_profit, 2),
        'Return_Percent': round(return_percent, 2)
        }
    
    # Run each model on current dataset and save predictions in dictionary
    for model in models:
        model_name = model.__name__   
        model_name = model_name.split('.')[-1]
        
        print(f'Starting Model {model_name}...')
        
        # Handle Run_Bot() Functionality of Models
        try:
            if model_name == 'Main_LogReg':
                pred_price = 0
                pct, curr_price, metrics = model.Run_Bot(data_path, FORECAST_DAYS)
            elif model_name == 'VersionVideo':
                pct, pred_price, curr_price, metrics = model.Run_Bot(data_path, ticker, FORECAST_DAYS, PLOT)
            else:
                pct, pred_price, curr_price, metrics = model.Run_Bot(data_path, ticker, LOOKBACK_DAYS, FORECAST_DAYS, PLOT)
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

print('\n-------------------------Phase 2: Sorting and Saving Dictionaries-------------------------')
## Load saved dictionaries (this is for if any market orders failed)
#print('\nSaved (sorted) Dictionary is:\n')
#print('*********************************************************************\n')
#Dict_Stock_Predictions = Load_Stocks_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_All')
#Dict_Trad_Stocks = Load_Trad_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_All')


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


#print(f'\nThe top {STOCKS_TO_PURCHASE} predicted stocks for each bot are as follows:')
#pprint(Dict_Top_Stock_Predictions)


# Save the full dictionary and the top stock predictions dictionary
Save_Stocks_Dictionary(Dict_Stock_Predictions, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_All')
Save_Stocks_Dictionary(Dict_Top_Stock_Predictions, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Best')
Save_Trad_Dictionary(Dict_Trad_Stocks, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_All')
Save_Trad_Dictionary(Dict_Top_Trad_Stocks, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_Best')




# Complete any BUY/SELL order requests and rank models
print('\n-------------------------Phase 3: Submit BUY/SELL Requests-------------------------')
# Make a dictionary that catches any failed BUY or SELL requests to be manually completed later
Dict_Failed_Requests = {}
Dict_Ranked_Models = {}

for model in models:
    model_name = model.__name__   
    model_name = model_name.split('.')[-1]
    
    # Make a trading client
    trading_client = alpaca_helper.GetTradingClient(getattr(configML, f'CONST_ALPACA_KEY_{model_name}'), getattr(configML, f'CONST_ALPACA_SECRET_{model_name}'))
    
    # Add the model name and its total account value to the model list
    total_equity, total_cash = alpaca_helper.GetAccountValue(trading_client)
    Dict_Ranked_Models[model_name] = total_equity
    
    print(f'\nFor model {model_name}; Total equity is: {total_equity}, total cash is: {total_cash}')
    
    # Complete the SELL order requests
    Dict_Current_Positions = alpaca_helper.GetCurrentPositions(trading_client)
    
    for ticker in Dict_Current_Positions:
        curr_pct_change = Dict_Current_Positions[model_name][ticker]['Current_Price'] / Dict_Current_Positions[model_name][ticker]['Average_Entry_Price']
        
        # If the current gains are greater than the next predicted gains or lower than 2% loss, then sell the stock
        if curr_pct_change > Dict_Top_Stock_Predictions[model_name][ticker]['Predicted_Returns'] or curr_pct_change < 0.98:
            print(f'Selling {(Dict_Current_Positions[ticker]['Quantity']):.2f} shares of {ticker} for model {model_name}')
            
            try:
                alpaca_helper.SellStock(trading_client, ticker, Dict_Current_Positions[ticker]['Quantity'])
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
        
    # Complete the BUY order requests
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
    

# Complete the buy orders for the traditional bot 
# These do not require a sell order since they will auto sell when they reach a specific price    
trading_client = alpaca_helper.GetTradingClient(configML.CONST_ALPACA_KEY_Trad, configML.CONST_ALPACA_SECRET_Trad)

# Add the model name and its total account value to the model list
total_equity, total_cash = alpaca_helper.GetAccountValue(trading_client)
Dict_Ranked_Models['Trad'] = total_equity

print(f'\nFor trad model; Total equity is: {total_equity}, total cash is: {total_cash}')
for ticker in Dict_Top_Trad_Stocks:
    if Dict_Trad_Stocks[ticker]['Entry_Price'] != 0:
        quantity = round((total_cash * (0.75/STOCKS_TO_PURCHASE)) / Dict_Trad_Stocks[ticker]['Entry_Price'], 0)
        
        print(f'Buying {quantity} shares of {ticker} for traditional model')
        try:
            alpaca_helper.Buy_Stock_Traditional(trading_client, ticker, Dict_Trad_Stocks[ticker]['Stop_Loss'], Dict_Trad_Stocks[ticker]['Take_Profit'], quantity)
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
            
# Save the failed requests dictionary
# If the dictionary is empty then it won't be saved
if bool(Dict_Failed_Requests):
    Save_Stocks_Dictionary(Dict_Failed_Requests, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Failed_Requests')


# Sort the models based on their account value
print('\n-------------------------Phase 4: Rank Models-------------------------')
ranked_models = sorted(
    Dict_Ranked_Models.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print current model rankings
print('The current standings of the models are: ')
pprint(ranked_models)
Save_Rankings_Dictionary(ranked_models, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Rankings')

print('The models have finished running!')
print(datetime.now())
print('-------------------------Closing BotManager-------------------------')



