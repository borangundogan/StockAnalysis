import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from multiprocessing import Pool


def trading_algorithm(ticker_info=None, ticker_history=None):
    """
    This function implements a trading algorithm based on various signals including valuation metrics, technical analysis,
    market data, and financial metrics.
    
    Args:
        ticker_info (dict): A dictionary containing information about the stock.
        
    Returns:
        str: A recommendation to either buy, sell, or hold the stock.
    """
    # Step 1: Define thresholds and weights for decision-making
    buy_threshold = 0.7  # Threshold for buy signal
    sell_threshold = 0.3  # Threshold for sell signal
    valuation_weight = 0.3  # Weight for valuation metrics
    technical_weight = 0.3  # Weight for technical analysis
    market_weight = 0.2  # Weight for market data
    financial_weight = 0.2  # Weight for financial metrics
    
    # Step 2: Extract relevant parameters from the ticker information
    trailing_pe = ticker_info.get('trailingPE', 0)
    forward_pe = ticker_info.get('forwardPE', 0)
    dividend_yield = ticker_info.get('dividendYield', 0)
    volume = ticker_info.get('volume', 0)
    market_cap = ticker_info.get('marketCap', 0)
    fifty_two_week_low = ticker_info.get('fiftyTwoWeekLow', 0)
    fifty_two_week_high = ticker_info.get('fiftyTwoWeekHigh', 0)
    profit_margins = ticker_info.get('profitMargins', 0)
    return_on_equity = ticker_info.get('returnOnEquity', 0)
    trailing_eps = ticker_info.get('trailingEps', 0)
    forward_eps = ticker_info.get('forwardEps', 0)
    
    # Step 3: Apply signals based on the extracted parameters
    # Valuation Signals
    valuation_score = (trailing_pe + forward_pe + dividend_yield) / 3  # Calculate valuation score
    
    # Technical Analysis Signals (Assuming RSI and Moving Average Cross Signals)
    rsi_signal = calculate_rsi_signal(ticker_history)  # Calculate RSI signal
    print(f"RSI Signal: {rsi_signal}")
    
    ma_cross_signal = calculate_ma_cross_signal(ticker_history)  # Calculate moving average cross signal
    print(f"MA Signal: {ma_cross_signal}")

    # Market Data Signals
    market_score = (volume + market_cap + (fifty_two_week_high - fifty_two_week_low)) / 3  # Calculate market score
    
    # Financial Metrics Signals
    financial_score = (profit_margins + return_on_equity + trailing_eps + forward_eps) / 4  # Calculate financial score
    
    # Step 4: Combine signals and calculate overall score
    overall_score = (valuation_score * valuation_weight) + (rsi_signal * technical_weight) + \
                    (market_score * market_weight) + \
                    (financial_score * financial_weight)
    # (ma_cross_signal * technical_weight)
    normalization_overall_score = min_max_normalization(overall_score, 0, 10000000000)
    print(f"Trading Algorithm Overall Score: {normalization_overall_score}")

    # Step 5: Generate buy/sell/hold recommendation based on overall score
    if normalization_overall_score > buy_threshold:
        return "Buy"  # If overall score is above buy threshold, recommend buying
    elif normalization_overall_score < sell_threshold:
        return "Sell"  # If overall score is below sell threshold, recommend selling
    else:
        return "Hold"  # If overall score is between thresholds, recommend holding

def min_max_normalization(value, min_val, max_val):
    """
    Normalize a value using Min-Max Normalization.
    
    Args:
        value (float): The value to be normalized.
        min_val (float): Minimum value in the dataset.
        max_val (float): Maximum value in the dataset.
    
    Returns:
        float: Normalized value.
    """
    return (value - min_val) / (max_val - min_val)

# Helper functions for technical analysis signals
def calculate_rsi_signal(ticker_history):
    """
    Calculate RSI signal based on Relative Strength Index.
    
    Args:
        ticker_info (DataFrame): A Pandas DataFrame containing historical price data.
        
    Returns:
        float: RSI signal value.
    """
    # Extract relevant parameters from DataFrame / Multiple data 17!
    close_prices = ticker_history["Close"]
    # Calculate price differences
    price_diff = close_prices.diff()
    
    # Calculate gains and losses
    gains = price_diff.where(price_diff > 0, 0)
    losses = -price_diff.where(price_diff < 0, 0)
    
    # Calculate average gains and losses over a period
    window_length = 14  # RSI typically uses a 14-day period
    avg_gains = gains.rolling(window=window_length).mean()
    avg_losses = losses.rolling(window=window_length).mean()
    
    # Calculate relative strength (RS)
    rs = avg_gains / avg_losses
    
    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))
    
    # Return the last RSI value
    return rsi.iloc[-1]


def calculate_ma_cross_signal(ticker_history, short_window=50, long_window=200):
    """
    Calculate moving average cross signal.

    Args:
        ticker_history (DataFrame): A DataFrame containing historical price data.
        short_window (int): The window size for the short moving average.
        long_window (int): The window size for the long moving average.

    Returns:
        float: Moving average cross signal value.
    """
    # Extract closing prices from the ticker_history DataFrame
    closing_prices = ticker_history["Close"]
    # print(closing_prices)

    # Ensure that window sizes are smaller than the length of the data
    if short_window >= len(closing_prices) or long_window >= len(closing_prices):
        raise ValueError("Window sizes should be smaller than the length of the data.")

    # Calculate short and long moving averages
    short_ma = calculate_moving_average(closing_prices, short_window)
    long_ma = calculate_moving_average(closing_prices, long_window)

    # Determine the current position of short and long moving averages
    short_ma_current = short_ma[-1]
    long_ma_current = long_ma[-1]
    short_ma_previous = short_ma[-2]
    long_ma_previous = long_ma[-2]
    
    print("Short Moving Average Current Value:", short_ma_current)
    print("Long Moving Average Current Value:", long_ma_current)
    print("Short Moving Average Previous Value:", short_ma_previous)
    print("Long Moving Average Previous Value:", long_ma_previous)

    # Calculate moving average cross signal
    if short_ma_previous < long_ma_previous and short_ma_current > long_ma_current:
        ma_cross_value = 1  # Buy signal
    elif short_ma_previous > long_ma_previous and short_ma_current < long_ma_current:
        ma_cross_value = -1  # Sell signal
    else:
        ma_cross_value = 0  # No signal

    return ma_cross_value

import statistics

def calculate_moving_average(data, window):
    """
    Calculate the moving average of the given data.

    Args:
        data (list): List of numerical values.
        window (int): Window size for the moving average.

    Returns:
        list: Moving average values.
    """
    moving_avg = []
    for i in range(len(data) - window + 1):
        window_data = data[i:i+window]
        avg = statistics.mean(window_data)
        moving_avg.append(avg)
    return moving_avg

if __name__ == "__main__":
   
    trading_algorithm()
