import yfinance as yf
import json

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = {
            'symbol': symbol,
            'name': stock.info.get('longName', 'N/A'),
            'price': stock.info.get('currentPrice', 'N/A'),
            'currency': stock.info.get('currency', 'N/A'),
            'market_cap': stock.info.get('marketCap', 'N/A'),
            'pe_ratio': stock.info.get('trailingPE', 'N/A')
        }
        return json.dumps(data, indent=4)
    except Exception as e:
        return json.dumps({'error': str(e)}, indent=4)

if __name__ == '__main__':
    stock_symbol = input('Enter the stock symbol: ')
    data = fetch_stock_data(stock_symbol)
    print(data)
