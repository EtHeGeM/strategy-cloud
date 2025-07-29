# strategy/rsi_momentum.py
import pandas as pd
import ta  # pip install ta

def apply_rsi_momentum_strategy(df):
    df = df.copy()
    df['momentum'] = df['close'].diff(4)
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    df['buy_signal'] = (df['momentum'] > 0) & (df['rsi'] < 30)
    df['sell_signal'] = (df['momentum'] < 0) & (df['rsi'] > 70)

    return df
