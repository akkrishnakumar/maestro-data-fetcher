import pandas as pd

def fetchTickers():
    csv_file = "./indices/NIfty-Next-50-01-May-2025.csv"
    try:
        df_from_csv = pd.read_csv(csv_file)
        return df_from_csv.iloc[:, 0].tolist()
    except FileNotFoundError:
        print(f"Error: File not found at {csv_file}")    
    except Exception as e:
        print(f"Error reading CSV file: {e}")