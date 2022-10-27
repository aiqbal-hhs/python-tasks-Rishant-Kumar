#-------------------------------@Rishant Kumar--------------------------------#
##########   IMPORTS   ##########
from tkinter import *
from tkinter import ttk


##########   CLASS CODE   ##########
class Book:
    """The Book class stores the details of each Book and has methods to Sell 
    books, Restock books and calculates the amount of books sold and remaining 
    stock of these books"""
    def __init__(self, name, stock, sold):
        self.name = str(name)
        self.stock = int(stock)
        self.sold = int(sold)
        comic_list.append(self)

    # Sells a chosen comic
    def sell(self, amount):
        if amount <= self.stock:
            self.stock -= amount
            self.sold += amount
            print(self.stock)
            return True
        else:
            return False

    # Restocks a set amount of the chosen comic
    def restock(self, amount):
        if amount > 0:
            self.stock += amount
            print(self.stock)
            return True
        else:
            return False


##########   FUNCTION AND SETUP - COMIC WINDOW   ##########
# Creates a name list to store every comic name in
def create_name_list():
  name_list = []
  for comic in comic_list:
    name_list.append(comic.name)
  return name_list

# Reads the comic book.txt for the instances of the comic class
def get_data():
    comic_file = open(
    "G:\My Drive\DGT 200\GUI\Rishant - GUI assessment (91906-7)\comic book.txt"
    ,"r"
    )
    line_list = comic_file.readlines()

    for line in line_list:
        comic_data = line.strip().split(",")
        Book(*comic_data)

    comic_file.close()

# Creates a function that will update the summary
def update_summary():
    total_stock_sold = 0
    stock_string = ""
    stock_string += "List of Comics:\n\n"
    comic_file = open(
    "G:\My Drive\DGT 200\GUI\Rishant - GUI assessment (91906-7)\comic book.txt"
    ,"w"
    )

    # Append each comic's name, and stock to the current stock level label
    for comic in comic_list:
        stock_string += "{}: {}\n".format(comic.name, comic.stock)
        comic_int = int(comic.sold)
        total_stock_sold += comic_int
        comic_file.write("{},{},{}\n".format(comic.name,
        comic.stock, comic.sold))

    stock_string += "\nTotal Comics Sold: {}".format(total_stock_sold)
    comic_details.set(stock_string)
    comic_file.close()

# When sell radio button is pressed...
def mode_sell():
    print(mode_var.get())
    # hide amount label and entry widgets
    amount_label.grid_remove()
    amount_entry.grid_remove()
    # set chosen_mode from mode_list to "Sell"
    chosen_mode.set(mode_list[0])

# When restock radio button is pressed...
def mode_restock():
    print(mode_var.get())
    
    # show amount label and entry widgets
    amount_label.grid()
    amount_entry.grid()

    # set chosen_mode from mode_list to "Restock"
    chosen_mode.set(mode_list[1])

    # updates the amount to make the entry box blank
    amount.set("")

# Create a sell function
def sell_stock(comic):
    if comic.sell(amount.get()):
        action_feedback_label.config(fg="lime")
        action_feedback.set("Success! {} {} comics were sold.".format(
            amount.get(), comic.name))
    else:
        action_feedback_label.config(fg="red")
        action_feedback.set("Uh Oh! {} is out of stock.".format(comic.name))

# restock function
def restock_stock(comic):
    try:
        if comic.restock(amount.get()):
            action_feedback_label.config(fg="lime")
            action_feedback.set("Success! {} {} comics were restocked."
            .format(amount.get(), comic.name))
        else:
            action_feedback_label.config(fg="red")
            action_feedback.set("Please enter a positive integer."
            .format(comic.name))
    except:
        action_feedback_label.config(fg="red")
        action_feedback.set("Please enter a number.".format(comic.name))

# When Sell/Restock Button is pressed...
def manage_stock():
    for comic in comic_list:
        if chosen_comic.get() == comic.name:
            if mode_var.get() == "sell":
                amount.set(1)
                sell_stock(comic)
            elif mode_var.get() == "restock":
                restock_stock(comic)
            else:
                pass
    # Update the Summary GUI 
    update_summary()
    amount.set("")


##########   DECLEARING VARIABLES, LISTS AND CALLING FUNCTION(S)   ##########
# creating colour  Variables...
primary_color = "#03a9f4" # Deep Sky Blue
secondary_color = "#e91e63" # Ruby
message_box_color = "#242424" # Nero (light black)
accent_color = "#429EBD" # Pelorous
background_colour = "#053F5C" # Teal Blue

# Setup Lists
comic_list = []
mode_list = ['Sell', 'Restock']

# Creating instances of comic class
get_data()

# inital amount of books
#super_dude = Book("Super Dude", 8, 0)
#lizard_man = Book("Lizard Man", 12, 0)
#water_woman = Book("Water Woman", 3, 0)

comic_names = create_name_list()


##########   COMIC GUI CODE   ##########
# Create a window with a title
root = Tk()
root.title("Comic Book Stock Manager - © Rishant")

# Set color of color window background
root.configure(bg=background_colour)

# root frame
root_frame = Frame(root, width=300, height=300, bg=background_colour)
root_frame.pack(padx=10, pady=5)

# Top frame (row 0, column 0)
top_title_frame = Frame(root_frame, width=300, height=250, bg="black")
top_title_frame.grid(row=0, column=0, columnspan=2,
padx=10, pady=5, sticky="WE")

# Comic label - Heading (row 0, column 0)
title_label = Label(top_title_frame, text="Comic Book Stock Manager",
font=("Courier", "16", "bold"),
bg=primary_color, padx=240, pady=5, anchor="center")
title_label.grid(row=0, column=0, columnspan=1, padx=3, pady=3, sticky="N")

# Left frame (row 1, column 0)
left_frame = Frame(root_frame, width=300, height=250)
left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="NS")

# Current Stock Level label - (row 0, column 0)
current_stock_level_label = Label(left_frame, text="Current Stock Level",
font=("Courier", "16", "bold"), bg=secondary_color, borderwidth=3,
relief="raised", width=22, padx=10, pady=5)
current_stock_level_label.grid(row=0, column=0, columnspan=1,
padx=10, pady=10)

# Create and set comic details
comic_details = StringVar()
update_summary()

# Stock Details label - (row 1, column 0)
details_label = Label(left_frame, textvariable=comic_details,
font=("Courier", "12", "bold"), bg=accent_color, padx=10, pady=5)
details_label.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

# Right frame (row 1, column 1)
right_frame = Frame(root_frame, width=300, height=250)
right_frame.grid(row=1, column=1, padx=10, pady=5, sticky="NS")

# Stock Manager label - (row 0, column 0)
mode_label = Label(right_frame, text="Stock Manager",
font=("Courier", "16", "bold"), bg=secondary_color, borderwidth=3,
relief="raised", width=22, padx=10, pady=5)
mode_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Mode label - (row 1, column 0)
mode_label = Label(right_frame, text="Mode:", font=("Courier", "12", "bold"),
bg=accent_color, pady=2)
mode_label.grid(row=1, column=0, padx=10, pady=5, sticky="WE")

# Radiobutton LabelFrame - (row 1, column 1)
mode_label_frame = LabelFrame(right_frame, bd=0)
mode_label_frame.grid(row=1, column=1, columnspan=1,
padx=10, pady=5, sticky="W")

# Mode(Sell/Restock) Radiobutton
mode_var = StringVar()
mode_var.set("sell")

# Sell Radiobutton (row 0, column 0)
sell_radio = ttk.Radiobutton(mode_label_frame, text="Sell", value="sell",
variable=mode_var, command=lambda: mode_sell())
sell_radio.grid(row=0, column=0, padx=10, pady=2)

# Restock Radiobutton (row 0, column 1)
restock_radio = ttk.Radiobutton(mode_label_frame, text="Restock",
value="restock", variable=mode_var, command=lambda: mode_restock())
restock_radio.grid(row=0, column=1, padx=10, pady=2)

# Comic Combobox label - (row 2, column 0)
comic_combobox_label = Label(right_frame, text="Comic:",
font=("Courier", "12", "bold"), bg=accent_color, padx=10, pady=2)
comic_combobox_label.grid(row=2, column=0, columnspan=1,
padx=10, pady=5, sticky="WE")

# Comic Combobox
# Setup variable and option list for the account Combobox
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the comic - (row 2, column 1)
comic_combobox = ttk.Combobox(right_frame, textvariable=chosen_comic,
state="readonly", font=("Courier", "12"), width=20)
comic_combobox['values'] = comic_names
comic_combobox.grid(row=2, column=1, columnspan=1,
padx=10, pady=10, sticky="WE")

# Entry Amount label - (row 3, column 0)
amount_label = Label(right_frame, text="Amount:",
font=("Courier", "12", "bold"), bg=accent_color, padx=5, pady=2)
amount_label.grid(row=3, column=0, columnspan=1, padx=10, pady=5, sticky="WE")
amount_label.grid_remove()

# Comic Entry - (row 3, column 1)
# Create a variable to store the amount
amount = IntVar()
amount.set("")

# Create an entry to type in amount
amount_entry = Entry(right_frame, textvariable=amount,
font=("Courier", "12"), width=7)
amount_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="W")
amount_entry.grid_remove()

# Button text variable
chosen_mode = StringVar()
chosen_mode.set(mode_list[0])

# Create a Button to sell or restock comics - (row 4, column 0)
manage_stock_button = Button(right_frame, textvariable=chosen_mode,
font=("Courier", "12"),width=20, command=manage_stock, bg=accent_color)
manage_stock_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create an action feedback label - (row 4, column 0)
action_feedback = StringVar()
action_feedback.set("Welcome!")
action_feedback_label = Label(right_frame, textvariable=action_feedback,
font=("Courier", "12"), bg=message_box_color,
fg="white", wrap=290, padx=5, pady=2)
action_feedback_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main window loop
root.mainloop()
