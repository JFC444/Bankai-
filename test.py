import tkinter as tk 
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="green")
label1.pack()  

label2 = tk.Label(root, text="Label 2")
label2.pack() 

root.mainloop() 
