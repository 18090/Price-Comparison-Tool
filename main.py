#Price Comparison Tool
# ____________   IMPORTS ________________
# used to create a custom window for price comparison tool
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ____________   FUNCTIONS ________________

def compare_prices(store, product):
  # compare the prices of the given store and product
  price_difference = store[product] - min(store.values())
  return price_difference

def add_item_to_database():
    item = e_item.get()
    price = float(e_price.get())
    # Add code here to add the item and price to your database
    # For example, you could use a dictionary:
    prices[item] = price
    # Display a message to confirm that the item has been added to the database
    messagebox.showinfo('message', f"{item} added to database with price ${price:.2f}")


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
      store_name = prices.get(product)
      if store_name is None:
        raise KeyError('Product not found in database')
      calc_price_difference = compare_prices(store_name, store)
      display_calc_price_difference(calc_price_difference)

    except Exception as ep:
      messagebox.showerror('error', ep)
      return

    msg = 'Prices compared successfully!'

  messagebox.showinfo('message', msg)


def exit():
  window.quit()

# ____________   DATABASE ________________
# create a dictionary to store product and price information
prices = {
    "milk": {
        "countdown": 4.50,
        "pak n save": 4.39,
        "new world": 5.15
    },
    "bread": {
        "countdown": 3.99,
        "pak n save": 3.87,
        "new world": 4.19
    },
    "apples": {
        "countdown": 7.99,
        "pak n save": 8.29,
        "new world": 8.79
    }
}

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
                    text="Select store name:",
                    font=("Comic Sans", 14),
                    fg="black",
                    bg="#a7f2cd")

store_options = ["Countdown", "New World", "Pak N Save"]
selected_store = tk.StringVar()
selected_store.set(store_options[0])

e_store = tk.OptionMenu(window, selected_store, *store_options)
e_store.config(font=("Comic Sans", 14))
e_item = tk.Entry(window, font=("Comic Sans", 14))
e_price = tk.Entry(window, font=("Comic Sans", 14))
e_item.pack(pady=5)
e_price.pack(pady=5)


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
                        command=add_item_to_database)
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
