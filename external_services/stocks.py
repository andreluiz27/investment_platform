import yfinance as yf


def get_stock_price(ticker):
    """
    Get the last price of a stock.

    Args:
        ticker (str): The ticker symbol of the stock.

    Returns:
        float: The last price of the stock.
    """
    ticker = ticker + ".SA"
    stock = yf.Ticker(ticker)
    return stock.fast_info.get("lastPrice")
