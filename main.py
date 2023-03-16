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
# Labels for product, store and budget
lb_date = tk.Label(window,
                   text="Product: ",
                   font=('Arial', 12, "bold"),
                   fg="black",
                   bg="#F7DC6F")
lb_month = tk.Label(window,
                    text="Store : ",
                    font=('Arial', 12, "bold"),
                    fg="black",
                    bg="#F7DC6F")
lb_year = tk.Label(window,
                   text="Budget: ",
                   font=('Arial', 12, "bold"),
                   fg="black",
                   bg="#F7DC6F")


# Placing the elements on the screen
lb_heading.place(x=200, y=5)
lb_subheading.place(x=250, y=40)
lb_date.place(x=20, y=80)
lb_month.place(x=20, y=105)
lb_year.place(x=20, y=130)