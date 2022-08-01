from tkinter import *
from tkinter import ttk


# Check function
def check():
  print(radio_var.get())

# Create a window
root = Tk()
root.title("My GUI App")
#getting screen width and height of display
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))

# Create a frame for first 2 widgets
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)

# Create a label and add it to the window using pack()
label1 = ttk.Label(frame1, text="My GUI App!")
label1.grid(row=0, column=0, padx=10, pady=5)

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = ttk.Entry(frame1, textvariable=words)
words_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a frame for the second 2 widgets
frame2 = ttk.Frame(root)
frame2.grid(row=1, column=0)

# Create a second label with longer text and add it to the window using pack()
label2 = ttk.Label(frame2, textvariable=words, wraplength=150)
label2.grid(row=2, column=0, padx=10, pady=5)

# Create a StringVar() for the chosen option
chosen_option = StringVar()

# Create a list of items for the Option Menu
options = ['Vanilla', 'Strawberry', 'Chocolate']

# Create the option menu and place in row 3, column 0
option_menu = ttk.OptionMenu(frame2, chosen_option, options[0], *options)
option_menu.grid(row=3, column=0, padx=10, pady=5)

# Create a LabelFrame for the checkbuttons
frame3 = ttk.LabelFrame(root, text="Checkbuttons")
frame3.grid(row=2, column=0, padx=10, pady=10, sticky="WE")

# Create variables for 2 checkbuttons
check1_var = IntVar()
check2_var = IntVar()
check2_var.set(1)

# Create 2 check buttons
check1 = ttk.Checkbutton(frame3, text="Option 1", variable=check1_var, command=check)
check1.grid(row=0, column=0)

check2 = ttk.Checkbutton(frame3, text="Option 1", variable=check2_var, state="disabled")
check2.grid(row=1, column=0)

# Create a LabelFrame for the radiobuttons
frame4 = ttk.LabelFrame(root, text="Radiobuttons")
frame4.grid(row=3, column=0, padx=10, pady=10, sticky="WE")

#Create 3 radiobuttons
radio_var = StringVar()
radio1 = ttk.Radiobutton(frame4, text='Red', value='red', variable=radio_var)
radio1.grid(row=0, column=0)

radio2 = ttk.Radiobutton(frame4, text='Green', value='green', variable=radio_var)
radio2.grid(row=0, column=1)

radio3 = radio2 = ttk.Radiobutton(frame4, text='Blue', value='blue', variable=radio_var)
radio3.grid(row=0, column=2)

# Run the main window loop
root.mainloop()
