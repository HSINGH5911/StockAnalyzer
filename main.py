import tkinter as tk
from tkinter import ttk
from single import InputWindow
from mult import InputLevel


def open_input():
    InputWindow(root)

def open_multiple():
    InputLevel(root)

root = tk.Tk()
root.geometry("800x500")

welcome_style = ttk.Style()
welcome_style.configure('Welcome_Label.TLabel', font=('Times new roman', 24, 'bold'))

regular_style = ttk.Style()
regular_style.configure('Reg.TLabel', font=('Times new roman', 10))

ttk.Label(root, text="Welcome to the stock analyzer", style='Welcome_Label.TLabel').grid(row=0, column=1, pady=10)

ttk.Label(root, text="Open Single Ticker Comparison", style='Reg.TLabel').grid(row=2, column=0, padx = 10, pady=10)
ttk.Button(root, text="Open window", command=open_input).grid(row=2, column=1, pady=10, sticky=tk.W)

ttk.Label(root, text="View multiple ticker symbols", style='Reg.TLabel').grid(row=3, column=0, padx=10, sticky=tk.W)
ttk.Button(root, text="Open window", command=open_multiple).grid(row=3, column=1, pady=10, sticky=tk.W)
root.mainloop()
