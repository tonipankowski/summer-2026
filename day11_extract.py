import yfinance as yf
import pandas as pd
import argparse

def extract_data(ticker):
    data = yf.download(ticker, start="2024-01-01", end="2024-12-31")
    data.columns = data.columns.droplevel(1)
    return data

def save_data(data, filename):
    data.to_csv(filename)
    print(f"Saved data to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", default="AAPL")
    args = parser.parse_args()
    
    data = extract_data(args.ticker)
    save_data(data, f"data/{args.ticker}.csv")

# scheduling / cron concept
# command to run to schedule the script to run
# AUTOMATICALLY
# 0 18 * * *   python3 /path/to/day11_extract.py 
