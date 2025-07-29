# visual/chart_utils.py
import plotly.graph_objects as go
import pandas as pd

def plot_strategy_signals(df, title="Strateji Sinyalleri"):
    df = df.copy().dropna()

    fig = go.Figure()

    # Candlestick grafiği
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Fiyat',
        increasing_line_color='green',
        decreasing_line_color='red'
    ))

    # Al sinyali (yeşil yukarı ok)
    buy_signals = df[df['buy_signal']]
    fig.add_trace(go.Scatter(
        x=buy_signals.index,
        y=buy_signals['close'],
        mode='markers',
        marker=dict(symbol='triangle-up', size=10, color='lime'),
        name='Al Sinyali'
    ))

    # Sat sinyali (kırmızı aşağı ok)
    sell_signals = df[df['sell_signal']]
    fig.add_trace(go.Scatter(
        x=sell_signals.index,
        y=sell_signals['close'],
        mode='markers',
        marker=dict(symbol='triangle-down', size=10, color='red'),
        name='Sat Sinyali'
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Zaman",
        yaxis_title="Fiyat",
        xaxis_rangeslider_visible=False,
        template="plotly_dark",
        height=600
    )

    return fig
