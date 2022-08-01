# importing tkinter gui
from tkinter import *
from tkinter import ttk

#creating window
window=Tk()
 
#getting screen width and height of display
width = window.winfo_screenwidth()
height =window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("Geeeks For Geeks")
label = ttk.Label(window, text="Hello Tkinter!")
label.pack()
 
window.mainloop()