import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class InputLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Multiple")
        self.geometry("800x500")

        frm = ttk.Frame(self)
        frm.grid(padx=20, pady=20)

        LABEL_OPTS = dict(padx=5, pady=5, sticky="w")
        INPUT_OPTS = dict(padx=5, pady=5, sticky="w")

        frm.columnconfigure(0, weight=0)
        frm.columnconfigure(1, weight=1)

        ttk.Label(frm, text="Enter amount of tickers").grid(row=0, column=0, **LABEL_OPTS)
        self.selected_ticker = tk.StringVar(value="Enter amount")
        self.dropdown = ttk.Combobox(
            frm,
            textvariable=self.selected_ticker,
            values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            state="readonly",
            width=22
        )
        self.dropdown.grid(row=0, column=1, **INPUT_OPTS)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_labels)
        self.dynamic_labels = ttk.Frame(frm)
        self.dynamic_labels.grid(row=1, column=0, **LABEL_OPTS)
        self.dynamic_widgets = []


    def update_labels(self, event=None):

        for widget in self.dynamic_widgets:
            widget.destroy()

        self.dynamic_widgets.clear()

        num_tickers =int(self.selected_ticker.get())

        for i in range(num_tickers):
            label = ttk.Label(
                self.dynamic_labels,
                text=f"Ticker {i + 1}:",
            )
            label.grid(row=i, column=0)

            entry = ttk.Entry(self.dynamic_labels, width=20)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.W)

            self.dynamic_widgets.append(label)


