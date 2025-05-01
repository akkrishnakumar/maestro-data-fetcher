"""
Fetches 6 months of historical stock data for a given stock symbol using the jugaad_data library.
This script assumes you have a project virtual environment set up and jugaad-data installed.
"""

from fetch import fetch_stock_data

def main():
    """
    Main function to get stock symbol from user and fetch/display data.
    """
    stock_symbol = input("Enter the stock symbol (e.g., SBIN, INFY): ").upper()
    data = fetch_stock_data(stock_symbol)  # Get the DataFrame

    if data is not None:  # Check if data was successfully retrieved
        # Print the first few rows of the DataFrame
        print("\nFirst 5 rows of data:")
        print(data.head().to_string())

        # Print the columns and their data types
        print("\nColumn information:")
        print(data.info())

if __name__ == "__main__":
    main()

