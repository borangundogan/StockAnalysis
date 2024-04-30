import yfinance as yf
import buy_sell_algorithm
import trading_algorithm


def main(): 
    ticker_symbol = "TKNSA.IS"
    
    # Create Ticker object
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    history_data = ticker.history(period="1mo")
    print("------------------------------------------------------------------")
    print("---------------------------*****----------------------------------")
    print("------------------------------------------------------------------")

    print(f"Ticker Name: {ticker_symbol}")
    print("---------------------------*****----------------------------------")


    # Call buy_sell_algorithm with ticker_info argument
    buy_sell_signal = buy_sell_algorithm.buy_sell_algorithm(ticker_info=info)
    print("Buy/sell signal:", buy_sell_signal)

    print("---------------------------*****----------------------------------")

    # Call trading_algorithm with ticker_info argument
    trading_signal = trading_algorithm.trading_algorithm(ticker_info=info, ticker_history=history_data)
    print("Trading signal:", trading_signal)
    print("------------------------------------------------------------------")
    print("---------------------------*****----------------------------------")
    print("------------------------------------------------------------------")
    
    return 0
if __name__ == "__main__":
    main()