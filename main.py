#Price Comparison Tool
# ____________   IMPORTS ________________
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ____________   FUNCTIONS ________________

def compare_prices(store, product):
  # compare the prices of the given store and product
  price_difference = store.price - product.price
  return price_difference


def display_calc_price_difference(price_difference):
  tbox_price_difference.config(state='normal')

  #price difference calculated is inserted into the text box after clearing the previous info in the textbox.
  tbox_price_difference.delete('1.0', tk.END)
  tbox_price_difference.insert(tk.END, price_difference)
  tbox_price_difference.config(state='disabled')


def validation():
  # gets the two entries
  store = e_store.get()
  product = e_product.get()
  msg = ''

  if len(store) == 0 or len(product) == 0:
    msg = 'store and product can\'t be empty'
  else:
    try:
      # msg = 'Success!'
      store_name = store
      product_name = product
      calc_price_difference = compare_prices(store_name, product_name)
      display_calc_price_difference(calc_price_difference)

    except Exception as ep:
      messagebox.showerror('error', ep)

  if msg != '':
    messagebox.showinfo('message', msg)


def exit():
  window.destroy()


# _____________ UPDATED DATABASE ________________
# data for product and prices to be stored here
if product == "milk":
  if store == "countdown":
    print("The price of Meadow Fresh 2L Milk at Countdown is currently $4.50. That's $0.11 more expensive than the cheapest option, Pak 'N' Save, at $4.39.")
  elif store == "pak n save":
    print("The price of Meadow Fresh 2L Milk at Pak 'N' Save is $4.39. This is the cheapest price of the supermarkets avaliable.")
  elif store == "new world":
    print("The price of Meadow Fresh 2L Milk at New World is currently $5.15. That's $0.76 more expensive than the cheapest option, Pak 'N' Save, at $4.39.")
elif product == "bread":
  if store == "countdown":
    print("The price of Tip Top White Toast Bread at Countdown is currently $3.99. That's $0.12 more expensive than the cheapest option, Pak 'N' Save, at $3.87.")
  elif store == "pak n save":
    print("The price of Tip Top White Toast Bread at Pak 'N' Save is currently $3.87. This is the cheapest price of the supermarkets avaliable.")
  elif store == "new world":
    print("The price of Tip Top White Toast Bread at New World is currently $4.19. That's $0.32 more expensive than the cheapest option, Pak 'N' Save, at $3.87.")
  

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
  text="Enter a product and a store.",
  fg="black",
  bg="#F7DC6F")

# Labels for product and store
lb_product = tk.Label(window,
                   text="Product: ",
                   font=('Arial', 12, "bold"),
                   fg="black",
                   bg="#F7DC6F")
lb_store = tk.Label(window,
                    text="Store : ",
                    font=('Arial', 12, "bold"),
                    fg="black",
                    bg="#F7DC6F")

# Entry boxes for product and store
e_product = tk.Entry(window, width=5)
e_store = tk.Entry(window, width=5)

# Button to calculate age
btn_price = tk.Button(window,
                              text="See the best price!",
                              font=("Arial", 13),
                              command=validation)

# Placing the elements on the screen
lb_heading.place(x=200, y=5)
lb_subheading.place(x=250, y=40)
lb_product.place(x=20, y=80)
lb_store.place(x=20, y=120)
