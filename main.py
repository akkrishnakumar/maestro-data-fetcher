"""
Fetches 6 months of historical stock data for a given stock symbol using the jugaad_data library.
This script assumes you have a project virtual environment set up and jugaad-data installed.
"""

from fetch import fetch_stock_data, fetch_stock_data_for_symbols
from fileUtils import fetchTickers
import pandas as pd

def main():
    
    # Fetch all tickers from a given NSE Index
    tickers = fetchTickers()

    data = fetch_stock_data_for_symbols(tickers) 

    print("\nFirst 3 symbols and their data:")
    for i, (symbol, data) in enumerate(data.items()):
        print(f"\nSymbol: {symbol}")
        if data is not None:
            print("Columns:", list(data.columns)) # Print the columns
            print(data.head().to_string())
        else:
            print("No data available.")
        if i >= 2:  # Stop after the first 3
            break

if __name__ == "__main__":
    main()

