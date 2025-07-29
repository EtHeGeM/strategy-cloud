from data.data_collector import get_yahoo_data
from strategy.rsi_momentum import apply_rsi_momentum_strategy
from strategy.backtest import backtest_strategy
from utils.warnings import get_disclaimer
from visual.chart_utils import plot_strategy_signals
import plotly.io as pio

# ... önceki kodlar ...


symbol = 'BTC-USD'
interval = '1h'

print("Veri çekiliyor...")
df = get_yahoo_data(symbol, interval=interval, period='30d')

print("Strateji uygulanıyor...")
df = apply_rsi_momentum_strategy(df)

print("Backtest çalıştırılıyor...")
results = backtest_strategy(df)

print("Sonuçlar:")
print(results)
print("\n" + get_disclaimer())

print("Grafik oluşturuluyor...")
fig = plot_strategy_signals(df, title=f"{symbol} - RSI+Momentum Stratejisi")
fig.show()  # Jupyter ya da localde açar
# pio.write_html(fig, "chart.html")  # İstersen HTML olarak kaydedebilirsin

