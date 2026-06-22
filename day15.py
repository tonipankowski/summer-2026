import yfinance as yf
import pandas as pd
import argparse
def extract_data(ticker):
    data = yf.download(ticker, start="2025-01-01", end="2025-12-31")
    if data.empty:
        print("Data is empty. Try again.")
        return data
    return data
def transform_data(data):
    data.columns = data.columns.droplevel(1)
    data["daily_return"] = data["Close"].pct_change()
    return data

def save_data(data, filename):
    data.to_csv(filename)
    print(f"Data saved to {filename}")
    
def show_data(data):
    print(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", default="^GSPC")
    args = parser.parse_args()
    
    data = extract_data(args.ticker)
    data = transform_data(data)
    save_data(data, f"data/{args.ticker}_day15.csv")
    show_data(data)