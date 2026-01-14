import tkinter as tk
from tkinter import ttk, messagebox


from input_window import InputWindow


def handle_input(ticker):
    print(ticker)

def open_input():
    InputWindow(root)

root = tk.Tk()
root.geometry("800x500")
ttk.Label(root, text="Open Single Ticker Comparison").grid(row=0, column=0)
ttk.Button(root, text="Open window", command=open_input).grid(row=0, column=1)
root.mainloop()
