import yfinance as yf
import pandas as pd

aapl = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
aapl.columns = aapl.columns.droplevel(1)

monthly = aapl["Close"].resample("ME").mean()

aapl["daily_return"] = aapl["Close"].pct_change()

aapl["prev_close"] = aapl["Close"].shift(1)

monthly_close = aapl["Close"].resample("ME").mean()
monthly_return = monthly_close.pct_change()


print(monthly)
print(aapl[["Close", "daily_return"]].head())
print(aapl[["Close", "prev_close"]].head())
print(monthly_return)
