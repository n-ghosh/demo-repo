# GUI testing 
import tkinter as tk

window = tk.Tk()
window.title("my GUI")
window.minsize(400,400)

# Why doesn't this work ?
greeting = tk.Label(master= window, text="Hello, Tkinter")
greeting.pack()

current_val = tk.DoubleVar()
slider = tk.Scale(master=window, from_=0, to=100, variable=current_val)
slider.pack()

window.mainloop()

# from tkinter import * 
# class Root(Tk):
#     def __init__(self):
#         super(Root,self).__init__()
 
#         self.title("Python Tkinter")
#         self.minsize(500,400)
 
# root = Root()
# root.mainloop()