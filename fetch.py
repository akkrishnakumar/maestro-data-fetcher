import pandas as pd
from datetime import date, timedelta
from jugaad_data.nse import stock_df  


def fetch_stock_data(symbol, months=6):
    """
    Fetches historical stock data for a given symbol for a specified number of months.

    Args:
        symbol (str): The stock symbol (e.g., 'SBIN', 'INFY').
        months (int, optional): The number of months of historical data to fetch. Defaults to 6.

    Returns:
        pandas.DataFrame: A pandas DataFrame containing the stock data, or None if an error occurs.
    """
    try:
        # Calculate the start and end dates
        end_date = date.today()
        start_date = end_date - timedelta(days=months * 30)  # Approximate months to days

        print(f"Fetching data for {symbol} from {start_date} to {end_date}...")

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