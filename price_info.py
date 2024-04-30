import yfinance as yf

# Hisse senedi simgesini belirtin
ticker_symbol = "AAPL"

# Ticker nesnesi oluşturun
ticker = yf.Ticker(ticker_symbol)

# Hisse senedi fiyat bilgilerini alın
price_info = ticker.history(period="1mo")  # Son 1 ayın fiyat bilgilerini alın

# Alınan verileri gösterin
print(price_info)
