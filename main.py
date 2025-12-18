import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


"""
Method To Make Sure The Dates Are Valid

:param start_date: Date to check
:param end_date: Date to check  
"""
def valid_dates(start, end):
    try:
        return datetime.strptime(start, "%Y-%m-%d") <= datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        return False

"""
Method To Send All Data To The Graph
"""
def submit():
    ticker = e_ticker.get().upper()
    start = e_start_date.get_date().strftime("%Y-%m-%d")
    end = e_end_date.get_date().strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)

    # Create The SMAs
    df["SMA_20"] = df["Close"].rolling(20).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()

    field = selected.get()
    if field not in df.columns:
        messagebox.showerror("Error", "Invalid Field")
        return

    if not valid_dates(start, end):
        messagebox.showerror("Error", "Invalid Date")
        return

    if df.empty:
        messagebox.showerror("Error", "No data found")
        return

    plt.figure(figsize=(8,8))

    plt.plot(df.index, df[field])
    plt.plot(df.index, df["SMA_20"])
    plt.plot(df.index, df["SMA_50"])

    plt.title(ticker)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend([field, "SMA_20", "SMA_50"])
    plt.grid(True)
    plt.show()

"""
Clear The Fields
"""
def clear():
    e_ticker.delete(0, tk.END)
    e_start_date.delete(0, tk.END)
    e_end_date.delete(0, tk.END)

    dropdown.set("")
    dropdown.set("Select Options")

"""
Clear All The Fields And Close All The Graphs That Have Been Made
"""
def clear_all():
    e_ticker.delete(0, tk.END)
    e_start_date.delete(0, tk.END)
    e_end_date.delete(0, tk.END)

    dropdown.set("")
    dropdown.set("Select Options")

    plt.close("all")

#Create The tkinter
root = tk.Tk()
root.geometry("800x500")
root.title("Stock Analyzer")

frm = ttk.Frame(root)
frm.grid(padx=20, pady=20)

#Creating Ticker Label
ttk.Label(frm, text="Enter ticker symbol").grid(row=0, column=0, padx=5, pady=5, sticky="w")
e_ticker = ttk.Entry(frm)
e_ticker.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#Asking For Start Date
ttk.Label(frm, text="Enter start date").grid(row=1, column=0, padx=5, pady=5, sticky="w")
e_start_date = DateEntry(frm, date_pattern="yyyy-mm-dd")
e_start_date.grid(row=1, column=1, padx=5, pady=5, sticky="w")

#Asking For End Date
ttk.Label(frm, text="Enter end date").grid(row=2, column=0, padx=5, pady=5, sticky="w")
e_end_date = DateEntry(frm, date_pattern="yyyy-mm-dd")
e_end_date.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#Asking What Data Field User Wants To See
ttk.Label(frm, text="Enter data field").grid(row=3, column=0, padx=5, pady=5, sticky="w")
options = ["Close", "High", "Low", "Open", "Volume"]
selected = tk.StringVar()
dropdown = ttk.Combobox(frm, textvariable=selected, values=options, state="readonly")
dropdown.grid(column=1, row=3, padx=5, pady=5, sticky="w")
dropdown.set("Select Options")


btn_frame = tk.Frame(frm)
btn_frame.grid(row=4, column=0, columnspan=3, pady=5)

#Submit Button
ttk.Button(btn_frame, text="Submit", command=submit).pack(side="left", padx=10)

#Clear Button
ttk.Button(btn_frame, text="Clear", command=clear).pack(side="left", padx=10)

#Clear All Button
ttk.Button(btn_frame, text="Clear All", command=clear_all).pack(side="left", padx=10)

root.mainloop()