###- TODOs
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
#           -Dim(Models * (Stocks * Metrics))
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
###!!! Add a system to see if a buy should be made when the program is run instead of just having to hope you are running the program on the correct dates
###!!! Increase speed 
#           -Maybe keep all dictionaries downloaded and just update them?
#           -Maybe save LSTM model so it only needs to be trained once ** NEED TO LOOK INTO THIS
###!!! Add randotron model?? (cat-yarn model)

###-



###- Import Statements
import BotManagerFunctions as Manager


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


from datetime import datetime
###-


###- Constants
models = [HistGrad, MultLSTM, LrgLSTM, MultVar, Pct, Raw, SglPred, LogReg, Video, Trad]

tickers = configML.CONST_STOCK_SYMBOLS

data_path = 'TrainCandles/TrainCandles'

Dict_Stock_Predictions = {}
Dict_Trad_Stocks = {}
STOCKS_TO_PURCHASE = 10
LOOKBACK_DAYS = 60
FORECAST_DAYS = 15
PLOT = False


# These are the phase constants to activate or deacativate a phase (ie: don't pull the most recent data)
PULL_DATA = True
PREDICT = True
SAVE_DICTS = True
LOAD_DICTS = False
BUY = True
SELL = True
RANK_MODELS = True

# This is to manually add code in case you want to run individually code snippets so you don't have to uncomment the whole thing
DEVELOPER_OVERRIDE = False
###- 


    
###!!!###- Main Loop -###!!!###
Dict_Failed_Requests = {}


if not DEVELOPER_OVERRIDE:
    print('-------------------------Starting BotManager-------------------------')
    
    #Train and Run all models and populate predictions into the dictionary
    if PULL_DATA:
        print('\n-------------------------Phase 1: Pulling Data and Predicting-------------------------')
        Manager.CreateDataCSVs(data_path, tickers)
    
    
    # Predict the stock prices and save the prediction dictionaries
    if PREDICT:
        print('\n-------------------------Phase 2: Making Stock Price Predictions-------------------------')
        Dict_Stock_Predictions, Dict_Trad_Stocks, Dict_Top_Stock_Predictions, Dict_Top_Trad_Stocks = Manager.MakePredictions(data_path, tickers, models, LOOKBACK_DAYS, FORECAST_DAYS, STOCKS_TO_PURCHASE, PLOT)
        
        print('\nPredictions Complete!')
    
        # Save the full dictionary and the top stock predictions dictionary
        if SAVE_DICTS:
            print('Saving dictionaries...')
            Manager.Save_Stocks_Dictionary(Dict_Stock_Predictions, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_All')
            Manager.Save_Stocks_Dictionary(Dict_Top_Stock_Predictions, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Best')
            Manager.Save_Trad_Dictionary(Dict_Trad_Stocks, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_All')
            Manager.Save_Trad_Dictionary(Dict_Top_Trad_Stocks, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_Best')
            
            print('Dictionaries saved successfully!')
    
    # Load the stock dictionaries if the program did not run successfully
    if LOAD_DICTS:
        print('\n-------------------------Load Stock Dictionaries-------------------------')
        Dict_Stock_Predictions = Manager.Load_Stocks_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_All')
        Dict_Top_Stock_Predictions = Manager.Load_Stocks_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_Best')
        Dict_Trad_Stocks = Manager.Load_Trad_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_All')
        Dict_Top_Trad_Stocks = Manager.Load_Trad_Dictionary('Saved_Dictionaries/' + str(datetime.now().date()) + '_Trad_Best')
    
    
    # Complete any BUY/SELL order requests and rank models
    if BUY or SELL:
        print('\n-------------------------Phase 3: Submit BUY/SELL Requests-------------------------')
        Dict_Failed_Requests = {}
        
        if BUY:
            Dict_Failed_Requests_Buy = Manager.CompleteBuyRequests(tickers, models, Dict_Stock_Predictions, Dict_Top_Stock_Predictions, Dict_Top_Trad_Stocks, STOCKS_TO_PURCHASE)
            Dict_Failed_Requests.update(Dict_Failed_Requests_Buy)
        if SELL: 
            Dict_Failed_Requests_Sell = Manager.CompleteSellRequests(tickers, models, Dict_Stock_Predictions)
            Dict_Failed_Requests.update(Dict_Failed_Requests_Sell)

        # Save the failed requests dictionary
        # If the dictionary is empty then it won't be saved
        print('\nBuy and Sell orders completed!')
        if bool(Dict_Failed_Requests):
            print('Saving failed buy sell requests...')
            Manager.Save_Stocks_Dictionary(Dict_Failed_Requests, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Failed_Requests')
        else:
            print('\nThere were no failed Buy or Sell Requests!')
        
        
    #Rank the models based on total equity 
    if RANK_MODELS:
        print('\n-------------------------Phase 4: Rank Models-------------------------')
        Dict_Ranked_Models = Manager.RankModels(models)
    
        print('\nSaving model rankings...')
        Manager.Save_Rankings_Dictionary(Dict_Ranked_Models, 'Saved_Dictionaries/' + str(datetime.now().date()) + '_Rankings')
        print('Model rankings have been saved!')
    
    print('-------------------------Closing BotManager-------------------------')
####!!!###- Main Loop -###!!!###




