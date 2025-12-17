import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
import tkinter as tk
from tkinter import ttk, messagebox

def valid_dates(start, end):
    try:
        return datetime.strptime(start, "%Y-%m-%d") <= datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        return False

def submit():
    ticker = e_ticker.get().upper()
    start = e_start_date.get()
    end = e_end_date.get()

    if not valid_dates(start, end):
        messagebox.showerror("Error", "Invalid Date")
        return

    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)

    if df.empty:
        messagebox.showerror("Error", "No data found")
        return

    df["SMA_20"] = df["Close"].rolling(20).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    plt.figure(figsize=(8,8))

    field = selected.get()
    if field not in df.columns:
        messagebox.showerror("Error", "Invalid Field")
        return

    plt.plot(df.index, df[field])
    plt.plot(df.index, df["SMA_20"])
    plt.plot(df.index, df["SMA_50"])

    plt.title(ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend([field, "SMA_20", "SMA_50"])
    plt.grid(True)
    plt.show()

root = tk.Tk()
root.geometry("800x500")

frm = ttk.Frame(root)
frm.grid(padx=20, pady=20)

ttk.Label(frm, text="Enter ticker symbol").grid(row=0, column=0, padx=5, pady=5, sticky="w")
e_ticker = ttk.Entry(frm)
e_ticker.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Enter start date").grid(row=1, column=0, padx=5, pady=5, sticky="w")
e_start_date = ttk.Entry(frm)
e_start_date.grid(row=1, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Enter end date").grid(row=2, column=0, padx=5, pady=5, sticky="w")
e_end_date = ttk.Entry(frm)
e_end_date.grid(row=2, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frm, text="Enter data field").grid(row=3, column=0, padx=5, pady=5, sticky="w")
options = ["Close", "High", "Low", "Open", "Volume"]
selected = tk.StringVar()
dropdown = ttk.Combobox(frm, textvariable=selected, values=options, state="readonly")
dropdown.grid(column=1, row=3, padx=5, pady=5, sticky="w")
dropdown.set("Select Options")

ttk.Button(frm, text="Submit", command=submit).grid(column=2, row=3, padx=5, pady=5, sticky="w")

root.mainloop()