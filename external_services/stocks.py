import yfinance as yf


def get_stock_price(ticker):
    ticker = ticker + ".SA"
    stock = yf.Ticker(ticker)
    return stock.fast_info.get("lastPrice")
