import bydate, byname, byextension

# path = "/Users/chunheiyue/Documents/tmp/"

# decision = input()

# if decision == "1":
#     bydate.datefunc(path)
# elif decision == "2":
#     byname.namefunc(path)
# elif decision == "3":
#     byextension.extensionfunc(path)



import tkinter as tk
import tkinter.ttk as ttk
import os
from tkinter import messagebox

def process_decision():
    # global e1  
    path = e1.get()

    while not os.path.exists(path):
        messagebox.showinfo("Error", "Path does not exist, enter another path!")
        e1.delete(0, tk.END)  
        e1.focus_set() 
        tk.mainloop()  

    decision = box.get()
    
    if decision == "By date":
        bydate.datefunc(path)
    elif decision == "By name":
        byname.namefunc(path)
    elif decision == "By file_extension":
        byextension.extensionfunc(path)

master = tk.Tk()

tk.Label(master, text='Path').grid(row=0)
e1 = tk.Entry(master)
e1.grid(row=0, column=1)

box = ttk.Combobox(master)
box["values"] = ["By date", "By name", "By file_extension"]
box.grid(row=1, columnspan=2, pady=15)
box.current(0)

button_process = tk.Button(master, text="Process", command=process_decision)
button_process.grid(row=2, columnspan=2, pady=10)

tk.mainloop()


