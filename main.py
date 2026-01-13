import tkinter as tk
from tkinter import ttk, messagebox


from input_window import InputWindow


def handle_input(ticker):
    print(ticker)

def open_input():
    InputWindow(root)

root = tk.Tk()
root.geometry("800x500")
ttk.Button(root, text="Open singular stock", command=open_input).pack()
root.mainloop()
