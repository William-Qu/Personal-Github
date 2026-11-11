# -*- coding: utf-8 -*-
###- Import Statements 
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed
###-

###- Global Variables
ALPACA_KEY = "PKYISF27TXAXUXHYQR5GOBXTZX"
ALPACA_SECRET = "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc"
###- 

###- Function Definitions
from alpaca.data.live import StockDataStream
from alpaca.data.enums import DataFeed

async def handle_trade(data):
    print("========== TRADE ==========")
    print(data)

async def handle_quote(data):
    print("========== QUOTE ==========")
    print(data)

stream = StockDataStream(
    ALPACA_KEY,
    ALPACA_SECRET,
    feed=DataFeed.IEX
)

stream.subscribe_trades(handle_trade, "AAPL")
stream.subscribe_quotes(handle_quote, "AAPL")

print("Starting connection to Alpaca...")

stream.run()
'''
# How to get current positions and their prices
trading_client = TradingClient("PKYISF27TXAXUXHYQR5GOBXTZX", "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc")

positions = trading_client.get_all_positions()
#trading_client.close_all_positions(cancel_orders=True) #Liquidates account

print(positions)
for position in positions:
    print(position.symbol, position.current_price)
'''


'''
# How to get current order requests and cancel them
trading_client = TradingClient("PKYISF27TXAXUXHYQR5GOBXTZX", "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc")

request_params = GetOrdersRequest(
    status=QueryOrderStatus.OPEN
    )

orders = trading_client.get_orders(request_params)

print(orders)

for order in orders:
    print("#####")
    print(order.id)
    trading_client.cancel_order_by_id(order.id)
'''


'''
# How to make a market and limit order request
trading_client = TradingClient("PKYISF27TXAXUXHYQR5GOBXTZX", "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc")

market_order_data = LimitOrderRequest(
    symbol="SPY", 
    qty=1, 
    side=OrderSide.BUY, #Buying or selling
    time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
    limit_price = 780.0 #The amount that caps at how much were willing to buy at
    )

market_order_data = MarketOrderRequest(
    symbol="SPY", 
    qty=1, 
    side=OrderSide.BUY, #Buying or selling
    time_in_force=TimeInForce.DAY, #How long will it wait before expiring the request
    )

market_order = trading_client.submit_order(market_order_data)
print(market_order)
'''

'''
# Basic data retrieval for stock bar prices
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

client = StockHistoricalDataClient("YOUR_API_KEY", "YOUR_API_SECRET")

request_params = StockBarsRequest(
    symbol_or_symbols="AAPL",
    timeframe=TimeFrame.Day,
    start=datetime(2024, 12, 2),
    end=datetime(2024, 12, 5)
)

bars = client.get_stock_bars(request_params)
print(bars.df)
'''

'''
# Basic data retrieval through the alpacas API
trading_client = TradingClient("PKYISF27TXAXUXHYQR5GOBXTZX", "DZiMGMhzGS36ot1GmXhqxuGRbxVRbNhRT4wRq7zHhVAc")

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)
print(trading_client.get_account().cash)


from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

data_client = StockHistoricalDataClient("PKYISF27TXAXUXHYQR5GOBXTZX", "")


request_params = StockTradesRequest(
    symbol_or_symbols="AAPL",
    start=datetime(2024, 12, 2, 10, 0),
    end=datetime(2024, 12, 3, 10, 1)
    )

trades = data_client.get_stock_trades(request_params)


print(trades)
print("hello there love")
'''