#Price Comparison Tool
# ____________   IMPORTS ________________
# used to create a custom window for price comparison tool
import tkinter as tk
from tkinter import messagebox

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
  # get user inputs for the new item
  store = e_store.get().lower()
  product = e_product.get().lower()
  price_str = e_price.get()
  msg = ''

  # validate inputs
  if not store or not product or not price_str:
    msg = 'store, product, and price can\'t be empty'
  else:
    try:
      price = float(price_str)
      if price <= 0:
        raise ValueError('Price must be a positive number')

      store_name = prices.get(product)
      if store_name is None:
        raise KeyError('Product not found in database')

      store[product][store_name] = price  # update the store dictionary with the new item
      calc_price_difference = compare_prices(store_name, product)
      display_calc_price_difference(calc_price_difference)

    except (ValueError, KeyError) as ep:
      messagebox.showerror('error', ep)
      return

    msg = 'Prices compared successfully!'

  messagebox.showinfo('message', msg)

def add_item():
    # get user inputs for the new item
    store = e_store.get().lower()
    product = e_product.get().lower()
    price_str = e_price.get()

    # validate inputs
    if not store or not product or not price_str:
        messagebox.showerror("Error", "Please enter a store, product, and price.")
        return
    try:
        price = float(price_str)
    except ValueError:
        messagebox.showerror("Error", "Price must be a number.")
        return

    # add the new item to the prices dictionary
    if product in prices:
        prices[product][store] = price
    else:
        prices[product] = {store: price}

    # reset the input fields
    e_store.setvar(selected_store, store_options[0])
    e_product.delete(0, tk.END)
    e_price.delete(0, tk.END)

    # show success message
    messagebox.showinfo("Success", f"Added {product} ({store}) for ${price:.2f}!")


def exit():
  window.quit()

# ____________   DATABASE ________________
# create a dictionary to store product and price information
prices = {}

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

lb_product = tk.Label(window,
                      text="Enter product name (e.g. Milk):",
                      font=("Comic Sans", 14),
                      fg="black",
                      bg="#a7f2cd")
e_product = tk.Entry(window, font=("Comic Sans", 14))

# Pack the store and product labels

lb_product.pack(pady=10)

# Pack the store and product entry fields
#e_store.pack(pady=5)
e_product.pack(pady=5)

# Labels for store and product entry fields
lb_store = tk.Label(window,
                    text="Select a store:",
                    font=("Comic Sans", 14),
                    fg="black",
                    bg="#a7f2cd")
lb_store.pack(pady=10)

store_options = ["Countdown", "New World", "Pak N Save"]
selected_store = tk.StringVar()
selected_store.set(store_options[0])

e_store = tk.OptionMenu(window, selected_store, *store_options)
e_store.config(font=("Comic Sans", 14))

# Pack the store label and dropdown
lb_store.pack()
e_store.pack(pady=5)

# price
lb_price = tk.Label(window,
                    text="Enter price:",
                    font=("Comic Sans", 14),
                    fg="black",
                    bg="#a7f2cd")
e_price = tk.Entry(window, font=("Comic Sans", 14))
lb_price.pack(pady=10)
e_price.pack(pady=5)

btn_add = tk.Button(window,
                    text="Add Item",
                    font=("Comic Sans", 14),
                    bg="#5DADE2",
                    fg="white",
                    command=add_item)
btn_add.pack(pady=10)

# Button to compare prices
btn_compare = tk.Button(window,
                        text="Compare Prices",
                        font=("Comic Sans", 14),
                        bg="#58D68D",
                        fg="white",
                       )
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
