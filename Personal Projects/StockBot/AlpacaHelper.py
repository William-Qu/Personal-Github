# These are helper functions that handle trading and statistics from Alpacas

###- Import Statements 
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.requests import GetOrdersRequest, MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.enums import Adjustment

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.requests import TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed
from alpaca.common.exceptions import APIError


import pandas as pd
###-

###- Function Definitions
CONST_ALPACA_KEY_MAIN = "PKYISF27TXAXUXHYQR5GOBXTZX"
CONST_ALPACA_SECRET_MAIN = "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc"


def GetTradingClient(KEY, SECRET):
    trading_client = TradingClient(KEY, SECRET)
    return trading_client


def GetCurrentPositions(trading_client):
    Dict_Current_Positions = {}

    positions = trading_client.get_all_positions()

    #print(positions)

    # Populate dictionary with current positions
    for position in positions:
        #print(position.symbol, position.avg_entry_price, position.current_price, position.qty)
        Dict_Current_Positions[position.symbol] = {
            'Average_Entry_Price': position.avg_entry_price,
            'Current_Price': position.current_price,
            'Quantity': position.qty
            }
    
        
    return Dict_Current_Positions


def BuyStock(trading_client, ticker, quantity):
    market_order_data = MarketOrderRequest(
        order_class=OrderClass.SIMPLE,
        symbol=ticker, 
        qty=quantity, 
        side=OrderSide.BUY,
        time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
        )

    _ = trading_client.submit_order(market_order_data)

    # Exception handled outside function
    #try:
    #    market_order = trading_client.submit_order(market_order_data)
    #    print(f'{quantity} shares of {ticker} have been requested to be bought with status {market_order.status}.')
    #except APIError as e:
    #    print(f'Market order request for {quantity} stocks bought of {ticker} have failed with status {e.status_code}')
    
    
def SellStock(trading_client, ticker, quantity):
    market_order_data = MarketOrderRequest(
        symbol=ticker, 
        qty=quantity, 
        side=OrderSide.SELL,
        time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
        )
    
    _ = trading_client.submit_order(market_order_data)

    # Exception handled outside function
    #try:
    #    market_order = trading_client.submit_order(market_order_data)
    #    print(f'{quantity} shares of {ticker} have been requested to be sold with status {market_order.status}.')
    #except APIError as e:
    #    print(f'Market order request for {quantity} stocks sold of {ticker} have failed with status {e.status_code}')


def GetAccountValue(trading_client):
    account = trading_client.get_account()
    return float(account.equity), float(account.cash)

def Buy_Stock_Traditional(trading_client, symbol, stop_loss_in, take_profit_in, quantity):    
    market_order_data = MarketOrderRequest(
        symbol=symbol, 
        qty=quantity, 
        side=OrderSide.BUY, #Buying or selling
        time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
        order_class=OrderClass.BRACKET,
        take_profit=TakeProfitRequest(limit_price=take_profit_in),
        stop_loss=StopLossRequest(stop_price=stop_loss_in)
        )
    
    market_order = trading_client.submit_order(market_order_data)
    
    #print(market_order)
    
    # Print success/failure message depending on the order placement status
    if market_order.failed_at == None:
        print(f"Market order successfully placed for {quantity} of {symbol}. Stop loss is: {stop_loss_in}. Take profit is: {take_profit_in}.")
    else:
        print(f"Market order placement for {quantity} of {symbol} failed.")


# This gets the tickers for the S&P500 stocks, only use this if an error occurs and modify the tickers in configML
def GetSP500Tickers():
    # This needs to be redownloaded every time from the S&P 500 wiki page
    url = "file:///C:/Users/789wi/Downloads/List%20of%20S&P%20500%20companies%20-%20Wikipedia.html"


    tickers = pd.read_html(url, match="Symbol")[0]["Symbol"].tolist()
    
    tickers = [t.replace(".", "-") for t in tickers]
        
    print(tickers)


