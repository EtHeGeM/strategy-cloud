# Strategy Cloud

Strategy Cloud is a backtesting environment for financial technical analysis. It enables users to develop, test, and visualize trading strategies using Python.

## Features

- **Backtesting Engine:** Simulate trading strategies on historical data.
- **Technical Indicators:** Includes RSI momentum and other strategies.
- **Data Collection:** Tools for collecting and preparing financial data.
- **Visualization:** Chart utilities for visualizing strategy performance.
- **LLM Assist:** Potential for AI-assisted features. Will be developed in next version

## Project Structure

```
strategy-cloud/
├── app.py                  # Main application entry point
├── data/                   # Data collection utilities
│   └── data_collector.py
├── llm_assist/             # (Reserved for LLM/AI features)
├── strategy/               # Trading strategies and backtesting
│   ├── backtest.py
│   ├── rsi_momentum.py
│   └── strategies.py
├── utils/                  # Utility functions
│   └── warnings.py
├── visual/                 # Visualization utilities
│   └── chart_utils.py
├── test_main.py            # Unit tests
├── .streamlit/             # Streamlit configuration
│   └── config.toml
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/) (for UI, if used)
- Required Python packages (see below)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/strategy-cloud.git
   cd strategy-cloud
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Create `requirements.txt` if not present, based on your imports.)*

### Usage

Run the main application:
```bash
python app.py
```
Or, if using Streamlit:
```bash
streamlit run app.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the