# data/data_collector.py
import yfinance as yf
import pandas as pd

def get_yahoo_data(symbol='BTC-USD', interval='1h', period='30d'):
    """
    Yahoo üzerinden geçmiş veri çek.
    Örnek semboller:
      - BTC-USD (Bitcoin)
      - AAPL (Apple)
      - TSLA (Tesla)
    """
    if interval not in ['1m', '2m', '5m', '15m', '30m', '1h', '1d', '1wk']:
        raise ValueError("Desteklenmeyen zaman dilimi.")

    data = yf.download(tickers=symbol, interval=interval, period=period, progress=False, auto_adjust = True)
    #data.dropna(inplace=True)
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
    data.columns = [str(col[0]).lower() for col in data.columns] 
    return data

# Örnek kullanım
if __name__ == '__main__':
    df = get_yahoo_data('BTC-USD', interval='1h', period='30d')
    print(df.tail())
