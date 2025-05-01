import pandas as pd
from datetime import date, timedelta
from jugaad_data.nse import stock_df  
from typing import List, Dict, Optional

def fetch_stock_data_for_symbols(symbols: List[str], months: int = 6) -> Dict[str, Optional[pd.DataFrame]]:
    all_data = {}
    for symbol in symbols:
        data = fetch_stock_data(symbol, months) 
        all_data[symbol] = data
    return all_data

def fetch_stock_data(symbol, months=6) -> Optional[pd.DataFrame]:
    try:
        # Calculate the start and end dates
        end_date = date.today()
        start_date = end_date - timedelta(days=months * 30)

        # Fetch the stock data into a pandas DataFrame
        df = stock_df(symbol=symbol, from_date=start_date, to_date=end_date, series="EQ")

        # Check if the DataFrame is empty
        if df.empty:
            print(f"No data found for {symbol} for the specified period.")
            return None  # Return None to indicate no data

        print(f"Successfully fetched data for {symbol}.")
        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        print(
            "Please ensure that the stock symbol is correct and that the jugaad-data library is installed and working "
            "in your virtual environment."
        )
        return None  # Return None to indicate an error