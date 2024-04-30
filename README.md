**README**

# Stock Analysis Script

## Overview
This script is designed to analyze stock data fetched from Yahoo Finance using the `yfinance` library. It allows users to input a list of stock symbols via a CSV file, fetch relevant data such as stock ratings, and display the data in a tabular format. Additionally, it provides an option to sort the data based on stock ratings and generate a bar plot for visualization.

## Features
- **Fetching Stock Data**: The script utilizes Yahoo Finance API to fetch stock data including stock ratings.
- **Data Display**: It displays the fetched data in a tabular format.
- **Sorting**: Users have the option to sort the displayed data based on stock ratings.
- **Data Visualization**: The script can generate a bar plot to visualize the stock ratings.
- **Error Handling**: It handles errors gracefully, logging them for debugging purposes.
- **Multiprocessing**: To improve efficiency, the script employs multiprocessing for fetching data for multiple stocks concurrently.
- **Logging**: Detailed logging is implemented to track the execution flow and any encountered errors.

## Prerequisites
- Python 3.x
- Required Python packages: `requests`, `csv`, `yfinance`, `pandas`, `matplotlib`
- Internet connection to fetch stock data from Yahoo Finance

## Usage
1. **Install Dependencies**: Ensure that all required Python packages are installed. You can install them via pip:
   ```
   pip install requests yfinance pandas matplotlib
   ```
2. **Prepare Stock List**: Create a CSV file containing a list of stock symbols, with one symbol per line.
3. **Run the Script**: Execute the script `main.py`. You'll be prompted to enter the filename of the CSV containing stock symbols and whether to sort the data.
4. **View Data**: After execution, the script will display the fetched stock data. If opted, it will also generate a bar plot for visualization.
5. **Save Successful Symbols**: Optionally, you can choose to save the symbols for which data was successfully fetched into another CSV file.

## Logging
- Logs are stored in a file named `myapp.log` in the same directory as the script.
- Log entries include timestamps, log levels, and detailed messages for better debugging.

## Additional Notes
- Ensure that the provided CSV file contains valid stock symbols.
- If any errors occur during execution, refer to the log file for detailed information.
- For further assistance or inquiries, feel free to contact the script maintainer.


This repository contains scripts for implementing stock trading algorithms based on various signals and metrics. The main scripts are `trading_algorithm.py`, `buy_sell_algorithm.py`, and `main.py`.

### `trading_algorithm.py`

This script implements a trading algorithm based on valuation metrics, technical analysis, market data, and financial metrics. It calculates an overall score for a stock and generates a recommendation to either buy, sell, or hold the stock based on predefined thresholds.

### Dependencies
- `yfinance`: Python package for retrieving market data from Yahoo Finance.
- `pandas`: Python library for data manipulation and analysis.
- `matplotlib`: Python plotting library for creating visualizations.
- `multiprocessing`: Python module for parallel computing.

### Installation
You can install the required dependencies using pip:

```bash
pip install yfinance pandas matplotlib
```

#### Usage
```python
import trading_algorithm

# Call trading_algorithm function with ticker_info and ticker_history arguments
trading_signal = trading_algorithm.trading_algorithm(ticker_info=ticker_info, ticker_history=ticker_history)
print("Trading signal:", trading_signal)
```

### `buy_sell_algorithm.py`

This script implements a simple buy/sell algorithm based on the provided ticker information. It calculates a recommendation mean and generates a recommendation to either buy, sell, or hold the stock based on predefined thresholds.

#### Usage
```python
import buy_sell_algorithm

# Call buy_sell_algorithm function with ticker_info argument
buy_sell_signal = buy_sell_algorithm.buy_sell_algorithm(ticker_info=ticker_info)
print("Buy/sell signal:", buy_sell_signal)
```

### `main.py`

This script serves as the main entry point for using the trading algorithms. It retrieves information about a stock using the Yahoo Finance API, then calls both `buy_sell_algorithm` and `trading_algorithm` functions to generate buy/sell and trading signals respectively.

#### Usage
```python
import yfinance as yf
import buy_sell_algorithm
import trading_algorithm

# Define the ticker symbol
ticker_symbol = "TKNSA.IS"

# Create Ticker object
ticker = yf.Ticker(ticker_symbol)
info = ticker.info
history_data = ticker.history(period="1mo")

# Call buy_sell_algorithm with ticker_info argument
buy_sell_signal = buy_sell_algorithm.buy_sell_algorithm(ticker_info=info)
print("Buy/sell signal:", buy_sell_signal)

# Call trading_algorithm with ticker_info and ticker_history arguments
trading_signal = trading_algorithm.trading_algorithm(ticker_info=info, ticker_history=history_data)
print("Trading signal:", trading_signal)
```

### Note
Before running the scripts, make sure you have installed all the dependencies and have access to the Yahoo Finance API.

### Disclaimer
The trading algorithms provided in these scripts are for educational purposes only and should not be considered as financial advice. Always conduct thorough research and consult with a financial advisor before making investment decisions.



