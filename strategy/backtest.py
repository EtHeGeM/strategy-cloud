# strategy/backtest.py
import pandas as pd

def backtest_strategy(df):
    df = df.copy()
    balance = 1000
    position = 0
    trades = []

    for i in range(1, len(df)):
        if df['buy_signal'].iloc[i] and position == 0:
            position = balance / df['close'].iloc[i]
            balance = 0
            trades.append(('BUY', df.index[i], df['close'].iloc[i]))
        elif df['sell_signal'].iloc[i] and position > 0:
            balance = position * df['close'].iloc[i]
            position = 0
            trades.append(('SELL', df.index[i], df['close'].iloc[i]))

    final_value = balance if position == 0 else position * df['close'].iloc[-1]
    roi = ((final_value - 1000) / 1000) * 100
    return {
        'initial_balance': 1000,
        'final_balance': final_value,
        'roi_percent': round(roi, 2),
        'trade_count': len(trades),
        'trades': trades
    }
