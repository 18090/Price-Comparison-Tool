#Price Comparison Tool
# ____________   IMPORTS ________________
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ____________   FUNCTIONS ________________

def compare_prices(store, product):
  # compare the prices of the given store and product
  price_difference = store[product] - min(store.values())
  return price_difference


def display_calc_price_difference(price_difference):
  tbox_price_difference.config(state='normal')

  #price difference calculated is inserted into the text box after clearing the previous info in the textbox.
  tbox_price_difference.delete('1.0', tk.END)
  tbox_price_difference.insert(tk.END, f"${price_difference:.2f}")
  tbox_price_difference.config(state='disabled')


def validation():
  # gets the two entries
  store = e_store.get().lower()
  product = e_product.get().lower()
  msg = ''

  if len(store) == 0 or len(product) == 0:
    msg = 'store and product can\'t be empty'
  else:
    try:
      # msg = 'Success!'
      store_name = prices[product]
      calc_price_difference = compare_prices(store_name, store)
      display_calc_price_difference(calc_price_difference)

    except Exception as ep:
      messagebox.showerror('error', ep)
      return

    msg = 'Prices compared successfully!'

  messagebox.showinfo('message', msg)


def exit():
  window.quit()


# create a dictionary to store product and price information
 if product == "milk":
    if store == "countdown":
        return ("The price of Meadow Fresh 2L Milk at Countdown is currently $4.50. That's $0.11 more expensive than the cheapest option, Pak 'N' Save, at $4.39.")
    elif store == "pak n save":
        return ("The price of Meadow Fresh 2L Milk at Pak 'N' Save is $4.39. This is the cheapest price of the supermarkets available.")
    elif store == "new world":
        return ("The price of Meadow Fresh 2L Milk at New World is currently $5.15. That's $0.76 more expensive than the cheapest option, Pak 'N' Save, at $4.39.")
elif product == "bread":
    if store == "countdown":
        return ("The price of Tip Top White Toast Bread at Countdown is currently $3.99. That's $0.12 more expensive than the cheapest option, Pak 'N' Save, at $3.87.")
    elif store == "pak n save":
        return ("The price of Tip Top White Toast Bread at Pak 'N' Save is currently $3.87. This is the cheapest price of the supermarkets available.")
    elif store == "new world":
        return ("The price of Tip Top White Toast Bread at New World is currently $4.19. That's $0.32 more expensive than the cheapest option, Pak 'N' Save, at $3.87.")
elif product == "apples":
    if store == "countdown":
        return ("The price of Jazz Apples at Countdown is currently $7.99/kg. That's $0.80 cheaper than the most expensive option, New World, at $8.79/kg.")
    elif store == "pak n save":
        return ("The price of Jazz Apples at Pak 'N' Save is $8.29/kg. That's $0.50 more expensive than the cheapest option, Countdown, at $7.99/kg.")
    elif store == "new world":
        return ("The price of Jazz Apples at New World is currently $8.79/kg. That's $0.80 more expensive than the cheapest option, Countdown, at $7.99/kg.")
    else:
        return ("Please enter a valid product.")

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

# Pack the heading label
lb_heading.pack(pady=20)

# Labels for store and product entry fields

lb_store = tk.Label(window,
                    text="Enter store name (e.g. Countdown):",
                    font=("Comic Sans", 14),
                    fg="black",
                    bg="#a7f2cd")
e_store = tk.Entry(window, font=("Comic Sans", 14))

lb_product = tk.Label(window,
                      text="Enter product name (e.g. Milk):",
                      font=("Comic Sans", 14),
                      fg="black",
                      bg="#a7f2cd")
e_product = tk.Entry(window, font=("Comic Sans", 14))

# Pack the store and product labels
lb_store.pack(pady=10)
lb_product.pack(pady=10)

# Pack the store and product entry fields
e_store.pack(pady=5)
e_product.pack(pady=5)

# Button to compare prices
btn_compare = tk.Button(window,
                        text="Compare Prices",
                        font=("Comic Sans", 14),
                        bg="#58D68D",
                        fg="white",
                        command=validation)
btn_compare.pack(pady=10)

# Text box to display the price difference
tbox_price_difference = tk.Text(window,
                                width=20,
                                height=2,
                                font=("Comic Sans", 14),
                                state='disabled')
tbox_price_difference.pack(pady=10)

# Button to exit the GUI
btn_exit = tk.Button(window,
                     text="Exit",
                     font=("Comic Sans", 14),
                     bg="#DC7633",
                     fg="white",
                     command=exit)
btn_exit.pack(pady=10)

# Run the main loop
window.mainloop()
