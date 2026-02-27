# Stock Fetching Tool

This repository contains tools for fetching stock data, specifically `stock_fetcher_yfinance.py` and `stock_fetcher.py`. This README will guide you through the installation process and provide usage examples.

## Installation

To install the necessary dependencies for the stock fetching tools, run:

```bash
pip install yfinance
```

## Usage

### 1. Using `stock_fetcher_yfinance.py`
This script uses the `yfinance` library to fetch stock data.

#### Example Usage:
```python
from stock_fetcher_yfinance import fetch_stock_data

# Fetch data for Apple Inc.
stock_data = fetch_stock_data('AAPL')
print(stock_data)
```

### 2. Using `stock_fetcher.py`
This script is a general stock fetching tool that may use various APIs or methods to retrieve stock data.

#### Example Usage:
```python
from stock_fetcher import fetch_stock_data

# Fetch data for Tesla Inc.
stock_data = fetch_stock_data('TSLA')
print(stock_data)
```

## Output Format

Both tools return data in the following JSON format:

```json
{
  "symbol": "AAPL",
  "open": 145.00,
  "close": 146.00,
  "high": 147.00,
  "low": 144.00,
  "volume": 1000000
}
```

Make sure to replace the stock symbol in the examples with the stock of your interest.