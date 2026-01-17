import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class InputLevel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title = "Multiple"
        self.geometry("800x500")
