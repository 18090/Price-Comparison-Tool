#Price Comparison Tool
# ____________   IMPORTS ________________
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ____________   MAIN  ________________
# Creating a custom window
window = tk.Tk()
window.geometry("700x500")
window.config(bg="#a7f2cd")
window.resizable(width=False, height=False)
window.title('Compare Prices Now!')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,
                      text="Price Comparison Tool!",
                      font=("Comic Sans", 20),
                      fg="black",
                      bg="#F7DC6F")
lb_subheading = tk.Label(
  window,
  font=("Arial", 12),
  text="Enter a store, a product, and a budget.",
  fg="black",
  bg="#F7DC6F")

# Placing the elements on the screen
lb_heading.place(x=200, y=5)
lb_subheading.place(x=250, y=40)