import yfinance as yf

def buy_sell_algorithm(ticker_info=None):
    """
    This function implements a simple buy/sell algorithm based on the provided ticker information.
    
    Args:
        ticker_info (dict): A dictionary containing information about the stock.
        
    Returns:
        str: A recommendation to either buy, sell, or hold the stock.
    """
    # Step 1: Define thresholds for decision-making
    buy_threshold = 1.5  # If recommendationMean is less than this threshold, consider buying
    sell_threshold = 2.5  # If recommendationMean is greater than this threshold, consider selling
    
    recommendation_mean = ticker_info.get('recommendationMean', 0)
    recommendation_key = ticker_info.get("recommendationKey")

    print(f"Recommendation Mean: {recommendation_mean}")
    print(f"Recommendation key: {recommendation_key}")
    
    # Step 3: Apply conditions based on the extracted parameters to make a recommendation
    if recommendation_mean < buy_threshold:
        return "Buy"  # If recommendationMean is high, consider buying
    elif recommendation_mean > sell_threshold:
        return "Sell"  # If recommendationMean is low, consider selling
    else:
        return "Hold"  # If recommendationMean is neither high nor low, hold the stock


if __name__ == "__main__":
    buy_sell_algorithm()