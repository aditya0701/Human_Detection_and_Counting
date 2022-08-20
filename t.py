
import sys
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

window=tk.Tk()

window.title("Running Python Script")
window.geometry('600x400')
    
def run():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)
    os.system('python main.py -i '+file_path)
def increment():
    
    ROOT = tk.Tk()

    ROOT.withdraw()
    os.system('python ./n.py')

btn =tk.Button(window, text="Video",command=run)
btn.place(x=5,y=160)
btn.grid(column=2, row=2)
btn1 =tk.Button(window, text="Config",command=increment)
btn1.place(x=5,y=160)
btn1.grid(column=4, row=2)
exit_button =tk.Button(window, text="Exit", command=window.destroy)
exit_button.place(x=5,y=160)
exit_button.grid(row=2,column=6)
window.mainloop()

