
## Introduction
This script uses the Interactive Brokers API to implement a trading algorithm. The algorithm uses data from the Yahoo Finance API and two different trading strategies: Moving Average Crossover and Bollinger Bands.

## Requirements
The following libraries and packages need to be installed:
run `pip install -r requirements` to install
- http
- ibapi
- yfinance
- pandas
- numpy
- matplotlib
- ib_insync

## Usage
The script consists of the following classes and functions:

### Classes
- MyClient
- MyEWrapper
- IBAPI

### Functions
- `get_stock_data(ticker)`
- `should_buy_or_sell(data)`
- `moving_average_crossover(data, short_window, long_window)`
- `bollinger_bands(data, window, num_std)`

#### `get_stock_data(ticker)`
This function takes a ticker symbol as input and returns a pandas dataframe with the stock's historical data.

#### `should_buy_or_sell(data)`
This function takes a pandas dataframe as input and returns a boolean indicating whether to buy or sell the stock based on the implemented trading strategy.

#### `moving_average_crossover(data, short_window, long_window)`
This function implements the Moving Average Crossover strategy. It returns a boolean indicating whether to buy or sell the stock.

#### `bollinger_bands(data, window, num_std)`
This function implements the Bollinger Bands strategy. It returns a boolean indicating whether to buy or sell the stock.

## Execution
download the script running `git clone https://github.com/dafrabzinator/STOCK_API.git`
The script is executed by calling the `should_buy_or_sell()` function and passing it the stock data. If the function returns True, the script connects to the Interactive Brokers API and executes a buy order. If the function returns False, the script connects to the Interactive Brokers API and executes a sell order :chart_with_upwards_trend:.

## Disclaimer 
Please note that this script is for educational purposes only and is not intended for use as an actual trading algorithm. Trading in the financial markets carries a high level of risk and is not suitable for all investors. Before making any investment decisions, it is important to carefully consider your investment objectives, level of experience, and risk appetite.

## Author :memo:
<a href="https://twitter.com/YourTwitterHandle">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter Logo" width="30" height="30">
</a>
:bust_in_silhouette: [Dafrabzinator](https://github.com/dafrabzinator)

<div align="center">
    <a href="https://twitter.com/YourTwitterHandle" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter Logo" width="50" height="50" hspace="20">
    </a>
    <a href="https://www.linkedin.com/in/YourLinkedInProfile" target="_blank">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn Logo" width="50" height="50" hspace="20">
    </a>
</div>

