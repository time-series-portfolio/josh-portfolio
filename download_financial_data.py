"""
Download Sports Betting & Entertainment stocks from Yahoo Finance
Saves daily price data and calculates returns/volatility metrics
"""

import yfinance as yf
import pandas as pd
import numpy as np
import os

# Create financial data directory if it doesn't exist
os.makedirs('data/financial', exist_ok=True)

print("=" * 70)
print("Downloading Sports Betting & Entertainment Stocks - Yahoo Finance")
print("=" * 70)

# Define sports betting and entertainment stocks
stocks = {
    'DKNG': {'name': 'DraftKings', 'start': '2020-04-23', 'note': 'IPO April 2020'},
    'PENN': {'name': 'Penn Entertainment (ESPN BET)', 'start': '2020-01-01', 'note': 'Barstool→ESPN BET'},
    'MGM': {'name': 'MGM Resorts (MGM BET)', 'start': '2020-01-01', 'note': 'Casino + Sportsbook'},
    'CZR': {'name': 'Caesars Entertainment', 'start': '2020-01-01', 'note': 'Caesars Sportsbook'},
    'DIS': {'name': 'Disney (ESPN)', 'start': '1980-01-01', 'note': 'Long-term baseline'}
}

# Download and process each stock
stock_data = {}

for i, (ticker, info) in enumerate(stocks.items(), 1):
    print(f"\n{i}. Downloading {ticker} ({info['name']})...")
    print(f"   Note: {info['note']}")
    print(f"   Date Range: {info['start']} to 2025-01-01")

    # Download data
    df = yf.download(ticker, start=info['start'], end='2025-01-01', progress=False, auto_adjust=False)

    # Flatten multi-level columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)

    print(f"   ✓ Downloaded {len(df)} trading days")

    # Calculate returns and volatility
    df['Returns'] = df['Adj Close'].pct_change()
    df['Log_Returns'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))
    df['Volatility_20d'] = df['Returns'].rolling(window=20).std()
    df['Volatility_60d'] = df['Returns'].rolling(window=60).std()
    df['Cumulative_Returns'] = (1 + df['Returns']).cumprod() - 1

    # Save to CSV
    filename = f'data/financial/{ticker}_daily.csv'
    df.to_csv(filename)
    print(f"   ✓ Saved to {filename}")

    stock_data[ticker] = df

# Summary statistics
print("\n" + "=" * 70)
print("Summary Statistics - Sports Betting Stocks")
print("=" * 70)

for ticker, df in stock_data.items():
    if ticker == 'DIS':
        continue  # Skip Disney for now

    print(f"\n{ticker} ({stocks[ticker]['name']}):")
    print(f"  Trading Days: {len(df)}")
    print(f"  Date Range: {df.index[0].date()} to {df.index[-1].date()}")
    print(f"  Mean Daily Return: {df['Returns'].mean():.4%}")
    print(f"  Volatility (Daily): {df['Returns'].std():.4%}")
    print(f"  Annualized Vol: {df['Returns'].std() * np.sqrt(252):.2%}")
    print(f"  Price Range: ${df['Adj Close'].min():.2f} - ${df['Adj Close'].max():.2f}")
    print(f"  Latest Price: ${df['Adj Close'].iloc[-1]:.2f}")
    if not df['Cumulative_Returns'].isna().all():
        print(f"  Total Return: {df['Cumulative_Returns'].iloc[-1]:.2%}")

print(f"\nDIS (Disney/ESPN) - Entertainment Baseline:")
print(f"  Trading Days: {len(stock_data['DIS'])}")
print(f"  Date Range: {stock_data['DIS'].index[0].date()} to {stock_data['DIS'].index[-1].date()}")
print(f"  Latest Price: ${stock_data['DIS']['Adj Close'].iloc[-1]:.2f}")

print("\n" + "=" * 70)
print("Financial Data Download Complete!")
print("=" * 70)
print("\nFiles created in data/financial/:")
for ticker in stocks.keys():
    print(f"  - {ticker}_daily.csv")
print("\nReady for time series analysis in R!")
print("\nSports Betting Context:")
print("  - COVID-19 (Mar 2020): Sports shutdown → online betting surge")
print("  - 2021-2022: Peak speculation bubble")
print("  - 2023-2025: Market maturation & consolidation")
