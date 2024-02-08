
## Introduction
This script uses the Interactive Brokers API to implement a trading algorithm. The algorithm uses data from the Yahoo Finance API and two different trading strategies:

## Usage
to clone this project, on your terminal run `git clone https://github.com/dafrabzinator/STOCK_API.git`. after the cloning process is complete, navigate into the project directory. 

here are some of the python packages specified in the requirements.txt file
- http
- ibapi
- yfinance
- pandas
- numpy
- matplotlib
- ib_insync
  
run `pip install -r requirements` to install all the required packages in your python environment. you can then execute the script.

### Functions
- `get_stock_data(ticker)`.
- `should_buy_or_sell(data)`.
- `moving_average_crossover(data, short_window, long_window)`.
- `bollinger_bands(data, window, num_std)`.

the `get_stock_data(ticker)` function takes a ticker symbol as input and returns a pandas dataframe with the stock's historical data.
![the stock data](/Figure_1.png)

`should_buy_or_sell(data)`
This function takes a pandas dataframe as input and returns a boolean indicating whether to buy or sell the stock based on the implemented trading strategy.

`moving_average_crossover(data, short_window, long_window)`
This function implements the Moving Average Crossover strategy. It returns a boolean indicating whether to buy or sell the stock.

`bollinger_bands(data, window, num_std)`
This function implements the Bollinger Bands strategy. It returns a boolean indicating whether to buy or sell the stock.

## Disclaimer 
Please note that this script is for educational purposes only and is not intended for use as an actual trading algorithm. Trading in the financial markets carries a high level of risk and is not suitable for all investors. Before making any investment decisions, it is important to carefully consider your investment objectives, level of experience, and risk appetite.



## Author :memo:
follow me on 
<div style="text-align: right;">
  <a href="https://twitter.com/dafrabs" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/twitter/twitter-original.svg" alt="Twitter Logo" width="30" height="20" style="margin-right: 20px;">
  </a>
  <a href="http://linkedin.com/in/oluwabusayomi-s-orosunlegan-6a0144263" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn Logo" width="30" height=" 20" style="margin-left: 20px;">
  </a>
</div>




