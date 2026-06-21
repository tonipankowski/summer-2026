import pandas as pd
import yfinance as yf
import argparse

def extract_data(ticker):
    data = yf.download(ticker, start="2024-01-01", end="2024-12-31")
    data.columns = data.columns.droplevel(1)
    return data

def save_data(data, filename):
    data.to_csv(filename)   
    print(f"Date saved to: {filename}")
    
def pct_return(data):
    monthly = data["Close"].resample("ME").mean()
    monthly_return = monthly.pct_change()
    return monthly_return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", default="AAPL")
    args = parser.parse_args()
    
    data = extract_data(args.ticker)
    if data.empty:
        print(f"Download failed for {args.ticker} - no data returned")
    else:
        print(pct_return(data))
        
    #print(pct_return(data))
    
     