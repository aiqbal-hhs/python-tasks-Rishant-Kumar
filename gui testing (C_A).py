from tkinter import *

# Create a window
root = Tk()
root.title("My GUI App")

# Create a label and add it to the window using pack()
label1 = Label(root, text="My GUI App!")
label1.pack()

#Create a StringVar() to store text
words = StringVar()

# Create a text entry field
words_entry = Entry(root, textvariable=words, bg="yellow", fg="red", selectbackground="limegreen", selectforeground="white")
words_entry.pack()

# Create a second label with longer text and add it to the window using pack()
label2 = Label(root, textvariable=words, wraplength=150)
label2.pack()

# Run the main window loop
root.mainloop()

