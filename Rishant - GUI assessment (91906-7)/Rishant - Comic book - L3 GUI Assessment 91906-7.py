from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# creating window
root = Tk()
# title of window
root.title("Comic Book Stock Manager - © Rishant")

# creating class
class Book:
  """The Book class stores the details of each Book and has methods to Sell books, Restock books and calculates the amount of books sold and remaining stock of these books"""
  def __init__(self, name, amount_sold, amount_of_books):
    self.name = name
    self.amount_sold = amount_sold
    self.amount_of_books = amount_of_books
    book_list.append(self)
  
  # restock method adds the amount of books to stock
  def restock(self, amount):
    if amount > 0:
      self.amount_of_books += amount
      return True
    else:
      return False
  
  # sell method subtracts one book from its stock and adds 1 to total number of books sold 
  def sell(self,):
    if 1 <= self.amount_of_books:
      self.amount_of_books -= 1
      self.amount_sold += 1
      return True
    else:
      return False
  


#lists
book_list = []

# Create instances of the class
super_dude = Book("Super Dude", 0, 8)
lizard_man = Book("Lizard Man", 0, 12)
water_woman = Book("Water Woman", 0, 3)

#account_names = create_name_list()

# Main GUI
# Create the stock level frame
stock_level_frame = ttk.LabelFrame(root, text="Current Stock Levels")
stock_level_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create the stock level frame
restock_level_frame = ttk.LabelFrame(root, text="Restock Comics")
restock_level_frame.grid(row=10, column=115, padx=10, pady=10, sticky="NSEW")

# text for each comic 
super_dude_text = StringVar()
super_dude_text.set("Super Dude: {}"#.format()
)

lizard_man_text = StringVar()
lizard_man_text.set("Lizard man: {}"#.format()
)

water_woman_text = StringVar()
water_woman_text.set("Water Woman: {}"#.format()
)

# Create and pack the label/texts for each 
super_dude_label = ttk.Label(stock_level_frame, textvariable=super_dude_text, wraplength=250)
super_dude_label.grid(row=5, column=5, columnspan=2, padx=10, pady=10)

lizard_man_label = ttk.Label(stock_level_frame, textvariable=lizard_man_text, wraplength=250)
lizard_man_label.grid(row=10, column=5, columnspan=2, padx=10, pady=10)

water_woman_label = ttk.Label(stock_level_frame, textvariable=water_woman_text, wraplength=250)
water_woman_label.grid(row=15, column=5, columnspan=2, padx=10, pady=10)

chosen_book_restock = StringVar()
chosen_book_restock.set(book_list[0])
# combobox for selecting the comic book to restock
comic_book_restock_combobox = ttk.Combobox(restock_level_frame, textvariable=chosen_book_restock, state="readonly")
chosen_book_restock['values'] = chosen_book_restock
comic_book_restock_combobox.pack()



root.mainloop()
