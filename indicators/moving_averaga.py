
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
        avg = sum(window_data) / window
        moving_avg.append(avg)
    return moving_avg
