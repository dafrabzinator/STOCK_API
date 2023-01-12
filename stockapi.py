#here we'll use the interactive Brokers Api
from http import client
import ibapi
from ibapi.client import EClient
import yfinance as yf 
#set up the environment 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
import time
from ib_insync import IB, util

class MyClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)
        # Initialize any necessary instance variables here
        pass
    
    # Add any additional methods or functionality here as required


class MyEWrapper(EWrapper):
    def __init__(self):
        # Initialize any necessary instance variables here
        pass
    
    # Override any necessary EWrapper methods here

#familiarize yourself with the api of your chosen brokerage
#create a class that subclasses the Ewrapper and Eclient classes provided by the interactive brokers api
class IBAPI(EClient):
    def __init__(self):
        EClient.__init__(self, MyEWrapper)
        self.connect("127.0.0.1", 7497, clientId=0)
        #here we use the yahhoofinancce APi and define a function takes a ticker symbol as input and returns adataframe with the stock's historical data
def get_stock_data(ticker):
            stock_data = yf.Ticker(ticker).history(period='1y')
            return stock_data
            #define  function that takes a dataframe and returns a boolean indicating wether to buy or sell the stock
def should_buy_or_sell(data):
    #implement your trading strategy here 
    return True # or False
    #test the algorithm and get the data for a stock
    data = get_stock_data("TSLA")
    #use the should_buy_or_sell function to determine whether to buy or sellvthe stock
    if should_buy_or_sell(data):
        #connect to the interactive Broken Api and execute a buy order
        api = IBAPI()
        api.connect("127.0.0.1",7497,clientId=0)
        api.placeOrder(...)
    else:
        #connect to the interactive brokers api and executeca sell order
        api = IBAPI()
        api.connect("127.0.0.1", 7497, clientId=0)
        api.placeOrder(...)
#moving average crossover strategy
def moving_average_crossover(data, short_window, long_window):
    """""Return a boolean indicating whether to buy or sell based on a moving average crossover strategy.
    Args:
    -data: a pandas dataframe with the stock's historical data.
    -short__window: an integer representing the number of days to use for the long moving average.
    -long window: an integer representing the number of days use for the long moving average.
    returns: 
    -a boolean indicating whether to buy(true) or sell(false) the stock.
    """
    #compute the moving averages.
    short_ma = data['Close'].rolling(window=short_window).mean()
    long_ma = data['Close'].rolling(window=long_window).mean()
    #if the moving average cross over the long moving average, it's a buy signal
    if (short_ma > long_ma).iloc[-2] and (short_ma <= long_ma).iloc[-1]:
        return True
    #if the moving average cross below the long movng average, it's a sell signal
    elif(short_ma < long_ma).iloc[-2] and (short_ma >= long_ma).iloc[-1]:
        return False
    #otherwise don't take any action
    else:
        return None
#Bollinger bands strategy
def bollinger_bands(data,window,num_std):
    """"Returns a boolean indicating whether to buy or sell based on a bollinger bands strategy.
    Args:
    -data: a pandas dataframe with the stock's historical data.
    -window: an integer representing the number of days to use for the moving average and standard deviation.
    -num_std: an integer representing the number of standard deviation to use for the upper and lower bands.
    Returns:
    - a boolean indicating whether to buy(True) or sell (false) the stock.
    """
    #compute the moving average and standard deviation
    ma = data['Close'].rolling(window=window).mean()
    std = data['Close'].rolling(window=window).std()
    #compute the upper and lower band.
    upper_band = ma+num_std*std
    lower_band = ma-num_std*std
    #if the stock's price touches the upper band ,it's a sell signal
    if (data['Close']>=upper_band).iloc[-1]:
        return False
    #if the stock's price touches lower band, it's a buy signal.
    elif(data['Close']<=lower_band).iloc[-1]:
        return True
    #otherwise, don't take any action.
    else:
        return None
#breakout strategy
def breakout(data,key_level):
    """return a  boolean indicating whether to buy or sell based on a breakout strategy.
    Args:
    -data: a pandas dataframe with the stock's historical data.
    -key_level: a float representing the key support or resistance level to watch for a breakout.
    -Returns:
    - a boolean indicating whether to buy(True) or sell(false) th stock.
"""
    #if the support breaks above resistance level it's a buy signal.
    if (data['High'].max()>key_level):
        return True
    #if the stock breaks below the suport level, it's a sell signal
    elif(data['High'].max()>key_level):
        return False
    #otherwise , don't take any actions.
    else:
        return None
#trend following strategy
def trend_following(data, indicator, long_window, short_window):
    """Returns a boolean indicating whether to buy or sell based on a trend following strategy;
    Args:
    -data: A pandas dataframe with the stock's historicsl data.
    -indicator: a string represneting the technical indicator to use (e.g 'ma' for moving average,'macd' for MACD) .
    -long_window: an integer representing the number of days to use for the long_term trend.
    -short_window: an integer representing the number of days to use for the short_term trend.
    -Returns:
    -A boolean indicating whether to buy(true) or sell(false) the stock.
    """
    #implement the trend following strategy using the chosen indicator
    if indicator == 'ma':
        #compute the moving averages.
        long_ma = data['Close'].rolling(window=long_window).mean()
        short_ma = data['Close'].rolling(window=short_window).mean()
        #if the short-term trend is above the long-term trend, it's a buy signal
        if (short_ma>long_ma).iloc[-1]:
            return True
        #if the short-term trend is below the long-term trend it's a sell signal
        elif(short_ma <long_ma).iloc[-1]:
            return False
        #otherwise, don't take any action
        else:
            return None
    elif indicator =='macd':
        #compute the MACD
        macd = data['Close'].ewm(span=long_window).mean()-data['Close'].ewm(span=short_window).mean()
        #if the MACD is positive, it's a buy signal
        if(macd>0).iloc[-1]:
            return True
        #if the MACD is negative, it's a sell signal
        elif(macd<0).iloc[-1]:
            return False
        #otherwise, don't take any action
        else:
            return None
    else:
        raise ValueError("invalid indicator. must be 'ma' or 'macd'.")
#mean reversion strategy
def mean_reversion(data, indicator, window):
    """ Returns a boolean indicating wheether to buy or sell based on a mean reversion strategy.
    Args:
    -data: A pandas dataframe with the stock's historical data.
    -indicator: a string representing the number of days to use (e.g. 'pe' for P/E RATIO,'zscore' fro z-score).
    -window:an integer representing the number of days to use for the indicator's historical average and standard dviation.
    Returns:
    -A boolean indicating whether to buy (True) or sell(false) the stock
    """
    #implement the mean reversion strategy using the chosen indicator
    if indicator == 'pe':
        #compute the p/e ratio and it's hiistorical average and standard deviation
        pe_ratio = data['Close']/data['Earnings per Share']
        ma = pe_ratio.rolling(window=window).mean()
        std = pe_ratio.rolling(window=window).std()
        #if the P/E ratio is more tha one standard deviation below the historical average, it's a buy signal
        if (pe_ratio<(ma-std)).iloc[-1]:
            return True
        #if the P/E ratio is more than one standard deviation above the historical average, it's a sell signal
        elif(pe_ratio<(ma-std)).iloc[-1]:
            return False
        #otherwise, don't take any actions
        else:
            return None
    elif indicator =='zscore':
        #compute the z-score and its hhistorical average and standard deviation
        zscore = (data['Close']-data['Close'].rolling(window=window).mean())/data['Close'].rolling(window=window).std()
        ma = zscore.rolling(window=window).mean()
        std = zscore.rolling(window=window).std()
        #if the zscore is more than one standard deviation below the historical average, it's a buy signal
        if (zscore<(ma-std)).iloc[-1]:
            return True
        #if the zscore is more than standard deviation above the historical average, its a sell signal
        elif(zscore>(ma+std)).iloc[-1]:
            return False
        #otherwise dont ake any action.
        else:
            return None
    else:
        raise ValueError("invalid indicator. must be 'pe' or 'zscore'.")

#Arbitrage strategy
def arbitrage(data, other_data):
   """Return boolean whether to buy or sell based on an arbitrage oppoertunity.
   Args:
   -data: a pandas dataframe with the stock's historical data.
   -other_dadta: a pandas dataframe with the data for the other market or asset to compare against.
   Returns:
   -A  boolean indicating whether to buy )True) or sell(False) the stock.
   """
   #if the stock's a undervalued relative to the other market or asset, it's a buy signal
   if (data['Close']<other_data['Close']).iloc[-1]:
    return True
   #if the stock's is overvalued relative to the other market or asset, it's a sell signal.
   elif(data['Close']>other_data['Close']).iloc[-1]:
    return False
   #otherwise  dont take actions.
   else:
    return None
#momentum strategy
def momentum(data,window):
    """Return a boolean indicating whethert to buy or sell based on a momentum stratgey.
    Arg:
    -data: A pandas dataframe with the stock's historical data.
    -window:an integer representing the number of days to use for the momentum calculation.
    Returns:
    -A boolean indicating whether to buy(True) or sell(False) the stock.
    """
    #compute the momentum.
    momentum = data['Close'].pct_change(periods=window)
    #if the momentum is poeitive, it's a buy signal
    if(momentum<0).iloc[-1]:
        return True
    #if the momentum is negative, it's a sell signal
    elif(momentum<0).iloc[-1]:
        return False
    #otherwise , don't take any actions.
    else:
        None

while True:
    data = get_stock_data("BTC") #retrieve new data
    plt.clf() # clear the existing chart
    plt.plot(data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title("dafrabs'sBTC Price chart")
    plt.draw() # redraw the chart
    plt.pause(1) # pause for 1 second

    if should_buy_or_sell(data):
        print("Buy")
    else:
        print("Sell")
    time.sleep(60) # sleep for 60 seconds before retrieving new data
from ib_insync import IB, util
import matplotlib.pyplot as plt

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=0)

# subscribe to real-time market data
contract = Stock('TSLA', 'SMART', 'USD')
ib.reqMktData(contract, '', False, False)

# create the plot
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title('Tesla Stock Price')
line, = ax.plot([], [])

# update the plot with new market data
def onTick(tick):
    time = util.parseIBDatetime(tick.time)
    line.set_data(time, tick.last)
    fig.canvas.draw()
    if should_buy_or_sell(tick.last):
        print("Buy")
    else:
        print("Sell")

ib.tickEvent += onTick
plt.show()
def should_buy_or_sell(tick):
    # Compare the bid and ask price to determine if there is a difference
    spread = tick.ask - tick.bid
    # Buy if the bid price is higher than the ask price
    if spread < 0:
        return True
    # Sell if the ask price is higher than the bid price
    elif spread > 0:
        return False
    # Otherwise, don't take any action
    else:
        return None
