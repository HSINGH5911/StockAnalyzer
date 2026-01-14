import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class InputWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Stock Analyzer")
        self.geometry("800x500")

        frm = ttk.Frame(self)
        frm.grid(padx=20, pady=20)

        ttk.Label(frm, text="Ticker", anchor="w").grid(row=0, column=0, sticky=tk.W)
        self.e_ticker = ttk.Entry(frm)
        self.e_ticker.grid(row=0, column=1)

        ttk.Label(frm, text="Start Date", anchor="w").grid(row=1, column=0, sticky=tk.W)
        self.e_start_date = DateEntry(
            frm,
            date_pattern="yyyy-mm-dd",
            state="readonly",
            showweeknumbers=False
        )

        self.e_start_date.grid(row=1, column=1, padx = 15, sticky=tk.W)

        ttk.Label(frm, text="End Date", anchor="w").grid(row=2, column=0, sticky=tk.W)
        self.e_end_date = DateEntry(frm, date_pattern="yyyy-mm-dd")
        self.e_end_date.grid(row=2, column=1, padx =15, sticky=tk.W)

        ttk.Label(frm, text="Field", anchor="w").grid(row=3, column=0, sticky=tk.W)
        self.selected = tk.StringVar(value="Close")
        self.dropdown = ttk.Combobox(
            frm,
            textvariable=self.selected,
            values=["Close", "Open", "High", "Low"],
            state="readonly",
        )
        self.dropdown.grid(row=3, column=1, padx = 15, sticky=tk.W)

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=4, column=0, columnspan=2)

        ttk.Button(btn_frame, text="Submit", command=self.submit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear).pack(side="left", padx=5)



    """
    # Method To Make Sure The Dates Are Valid

    #:param start_date: Date to check
    #:param end_date: Date to check
    """
    def valid_dates(self, start, end):
        try:
            return datetime.strptime(start, "%Y-%m-%d") <= datetime.strptime(end, "%Y-%m-%d")
        except ValueError:
            return False

    """
    # Method To Send All Data To The Graph
    """
    def submit(self):
        ticker = self.e_ticker.get().upper()
        start = self.e_start_date.get_date().strftime("%Y-%m-%d")
        end = self.e_end_date.get_date().strftime("%Y-%m-%d")
        df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)

        # Create The SMAs
        df["SMA_20"] = df["Close"].rolling(20).mean()
        df["SMA_50"] = df["Close"].rolling(50).mean()

        field = self.selected.get()
        if field not in df.columns:
            messagebox.showerror("Error", "Invalid Field")
            return

        if not self.valid_dates(start, end):
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
    # Clear The Fields
    """
    def clear(self):
        self.e_ticker.delete(0, tk.END)
        self.e_start_date.delete(0, tk.END)
        self.e_end_date.delete(0, tk.END)

        self.dropdown.set("")
        self.dropdown.set("Select Options")

    """
    # Clear All The Fields And Close All The Graphs That Have Been Made
    """
    def clear_all(self):
        self.e_ticker.delete(0, tk.END)
        self.e_start_date.delete(0, tk.END)
        self.e_end_date.delete(0, tk.END)

        self.dropdown.set("")
        self.dropdown.set("Select Options")

        plt.close("all")
