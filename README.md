
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

## Author :memo:<a href="https://twitter.com/dafrabzinator" target="_blank" title="Follow me on Twitter">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter Logo" width="30" height="30">
</a>
<style>
  /* Define the animation */
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
  }
  
  /* Apply the animation on hover */
  .icon:hover {
    animation: pulse 1s ease-in-out infinite;
  }
</style>

<a href="https://twitter.com/dafrabzinator" target="_blank" class="icon">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter Logo" width="30" height="30">
</a>
<style>
  /* Style the Twitter icon */
  .twitter-icon {
    fill: #1da1f2;
  }
  
  /* Style the LinkedIn icon */
  .linkedin-icon {
    fill: #0077b5;
  }
</style>

<a href="https://twitter.com/dafrabzinator" target="_blank" title="Follow me on Twitter">
  <svg class="twitter-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="30" height="30">
    <path d="M23.998 4.567c-.884.391-1.83.66-2.828.779 1.015-.611 1.798-1.574 2.168-2.723-.954.566-2.005.974-3.125 1.195-.896-.958-2.174-1.555-3.586-1.555-2.715 0-4.916 2.201-4.916 4.916 0 .386.044.76.129 1.119-4.08-.205-7.7-2.16-10.127-5.131-.422.722-.663 1.562-.663 2.463 0 1.702.866 3.207 2.182 4.086-.805-.026-1.56-.247-2.223-.614v.062c0 2.383 1.693 4.371 3.946 4.827-.414.113-.849.175-1.295.175-.316 0-.623-.029-.928-.085.626 1.937 2.445 3.348 4.603 3.385-1.682 1.319-3.802 2.104-



