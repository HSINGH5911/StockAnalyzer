import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

from websockets import Close


class Stock(Enum):
    Close = "Close"
    High = "High"
    Low = "Low"
    Open = "Open"
    Volume = "Volume"

def get_input():
    ticker = input('Enter ticker symbol: ').upper()
    start = input('Enter start date: ')
    end = input('Enter end date: ')
    want_to_see = int(input('What do you want to see: '))
    return ticker, start, end, want_to_see

def get_valid_dates(start, end):
    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        return start_date <= end_date
    except ValueError:
        return False


while True:
    ticker, start, end, want_to_see = get_input()

    stock_map = {
        1: Stock.Close,
        2: Stock.High,
        3: Stock.Low,
        4: Stock.Open,
        5: Stock.Volume
    }

    stock_choice = stock_map.get(want_to_see)
    column = stock_choice.value

    if not get_valid_dates(start, end):
        print('Invalid dates')
        continue

    try:
        df = yf.download(ticker, start = start, end = end, auto_adjust = True)
        if df.empty:
            print('No data')
        else:
            print(df.head(1))
    except Exception as e:
        print(f'Error: {e}')

    df["SMA_20"] = df["Close"].rolling(20).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    plt.figure(figsize = (10,5))
    plt.plot(df.index, df[column], label = column)
    plt.plot(df.index, df["SMA_20"], label = "SMA_20")
    plt.plot(df.index, df["SMA_50"], label = "SMA_50")

    plt.title(ticker)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

    again = input('Do you want to continue? (y/n): ').lower()

    if again == 'n':
        break