# strategy/strategies.py
import pandas as pd
import ta

def rsi_momentum(df):
    df = df.copy()
    df['momentum'] = df['close'].diff(4)
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    df['buy_signal'] = (df['momentum'] > 0) & (df['rsi'] < 30)
    df['sell_signal'] = (df['momentum'] < 0) & (df['rsi'] > 70)
    return df

def ema_crossover(df):
    df = df.copy()
    df['ema_fast'] = ta.trend.EMAIndicator(df['close'], window=12).ema_indicator()
    df['ema_slow'] = ta.trend.EMAIndicator(df['close'], window=26).ema_indicator()
    df['buy_signal'] = df['ema_fast'] > df['ema_slow']
    df['sell_signal'] = df['ema_fast'] < df['ema_slow']
    return df

def macd_crossover(df):
    df = df.copy()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['buy_signal'] = df['macd'] > df['macd_signal']
    df['sell_signal'] = df['macd'] < df['macd_signal']
    return df
