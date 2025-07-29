# app.py
import streamlit as st
from data.data_collector import get_yahoo_data
from strategy.rsi_momentum import apply_rsi_momentum_strategy
from strategy.backtest import backtest_strategy
from visual.chart_utils import plot_strategy_signals
from utils.warnings import get_disclaimer
from datetime import datetime
from strategy.strategies import rsi_momentum, ema_crossover, macd_crossover

## Developer : Eren Gemici - Yapay Zekanın Ta Kendisi
# ------------------ GÖMÜLÜ CSS ------------------
def inject_custom_css():
    st.markdown("""
        <style>
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        h1, h2, h3, h4 { color: #00FFB2; }
        section[data-testid="stSidebar"] {
            background-color: #1a1c25;
        }
        div[data-testid="metric-container"] {
            background-color: #1f222e;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #00FFB2;
        }
        .stPlotlyChart > div { max-height: 650px; }
        </style>
    """, unsafe_allow_html=True)

# ------------------ SAYFA AYARI ------------------
st.set_page_config(page_title="StrategyCloud", layout="wide")
inject_custom_css()

# ------------------ BAŞLIK ------------------
st.title("StrategyCloud")
st.caption("Strateji bazlı teknik analiz ve geçmiş performans test sistemi. Bu uygulama yatırım tavsiyesi içermez.")

st.markdown("---")

# ------------------ SIDEBAR SEÇİMLER ------------------
st.sidebar.header("Ayarlar")
symbol = st.sidebar.selectbox("Varlık Seçimi", ["BTC-USD", "ETH-USD", "AAPL", "TSLA", "SPY", "GOOG"])
interval = st.sidebar.selectbox("Zaman Aralığı", ["1h", "1d"])
period = st.sidebar.selectbox("Veri Dönemi", ["7d", "14d", "30d", "60d", "90d"])
show_table = st.sidebar.checkbox("İşlem Geçmişini Göster", value=True)
strategy_name = st.sidebar.selectbox(
    "Strateji Seçimi",
    ["RSI + Momentum", "EMA Crossover", "MACD Crossover"]
)


# ------------------ VERİ ÇEK ------------------
try:
    with st.spinner("Veri çekiliyor..."):
        df = get_yahoo_data(symbol, interval=interval, period=period)
except Exception as e:
    st.error(f"Veri alınırken hata oluştu: {e}")
    st.stop()

# ------------------ STRATEJİ ------------------
df = apply_rsi_momentum_strategy(df)

if strategy_name == "RSI + Momentum":
    df = rsi_momentum(df)
elif strategy_name == "EMA Crossover":
    df = ema_crossover(df)
elif strategy_name == "MACD Crossover":
    df = macd_crossover(df)


# ------------------ GRAFİK ------------------
st.subheader("Teknik Sinyal Grafiği")
st.markdown("Momentum + RSI stratejisine göre üretilen al/sat sinyalleri:")
fig = plot_strategy_signals(df, title=f"{symbol} - {strategy_name}")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ------------------ BACKTEST ------------------
st.subheader("Strateji Performansı (Backtest)")
results = backtest_strategy(df)

col1, col2, col3 = st.columns(3)
col1.metric("ROI (%)", f"{results['roi_percent']}%")
col2.metric("İşlem Sayısı", results['trade_count'])
col3.metric("Final Bakiye", f"${results['final_balance']:.2f}")

if show_table:
    st.markdown("İşlem Geçmişi")
    trades = results["trades"]
    if trades:
        trade_df = st.dataframe(
            {
                "İşlem Tipi": [t[0] for t in trades],
                "Zaman": [t[1].strftime("%Y-%m-%d %H:%M") if isinstance(t[1], datetime) else str(t[1]) for t in trades],
                "Fiyat": [round(t[2], 2) for t in trades]
            },
            use_container_width=True
        )
    else:
        st.info("Henüz işlem yapılmadı.")

st.markdown("---")

# ------------------ UYARI ------------------
st.warning(get_disclaimer())

st.markdown(
    "<div style='text-align: center; padding-top: 2rem;'>"
    "<small>© 2025 VisualQuant | Educational Use Only</small>"
    "</div>", unsafe_allow_html=True)
