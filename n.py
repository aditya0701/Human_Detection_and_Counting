# Program to make a simple
# login screen


import tkinter as tk
from tkinter import *
import re
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

root=tk.Tk()

# setting the windows size
root.geometry("600x400")
root.title("REAL TIME HUMAN DETECTION AND COUNTING")



# declaring string variable
# for storing name and password
Threshold_var=tk.StringVar()
Threshold_var.set("")
MAX_DISTANCE_var=tk.StringVar()
MAX_DISTANCE_var.set("")
MIN_DISTANCE_var=tk.StringVar()
MIN_DISTANCE_var.set("")
MAIL_var=tk.StringVar()
MAIL_var.set("")
url_var=tk.StringVar()
url_var.set("")



# defining function for email validation
def check(MAIL):
        if(re.search(regex, MAIL)):
                print("Valid Email")
 
        else:
                print("Invalid Email")







#defining Boolean variables for radio buttons
p=tk.BooleanVar()
p.set(True)
v=tk.BooleanVar()
v.set(True)
a=tk.BooleanVar()
a.set(True)
u=tk.BooleanVar()
u.set(True)
        

# defining a function that will
# get the name and password and
# print them on the screen
def submit():

	Threshold=Threshold_var.get()
	MAX_DISTANCE=MAX_DISTANCE_var.get()
	MIN_DISTANCE=MIN_DISTANCE_var.get()
	MAIL=MAIL_var.get()
	url=url_var.get()
	
	
	check(MAIL)
	pc=p.get()
	vc=v.get()
	ac=a.get()
	uc=u.get()
	
	print("The Threshold is : " + Threshold)
	print("The Maximum Distance is : " + MAX_DISTANCE)
	print("The Minimum Distance is : " + MIN_DISTANCE)
	print("The Email is : " + MAIL)
	print("The URL is : " + url)
	print("Show People Count : " + str(pc))
	print("Show Total Serious Violations : " + str(vc))
	print("Show Alert : " + str(ac))
	print("Use GPU : " + str(uc))
	
	
	

Threshold_label = tk.Label(root, text = 'THRESHOLD', font=('calibre',10, 'bold'))
Threshold_entry = tk.Entry(root,textvariable = Threshold_var, font=('calibre',10,'normal'))


MAX_DISTANCE_label = tk.Label(root, text = 'MAX DISTANCE', font = ('calibre',10,'bold'))
MAX_DISTANCE_entry=tk.Entry(root, textvariable = MAX_DISTANCE_var, font = ('calibre',10,'normal') )

MIN_DISTANCE_label = tk.Label(root, text = 'MIN DISTANCE', font = ('calibre',10,'bold'))
MIN_DISTANCE_entry=tk.Entry(root, textvariable = MIN_DISTANCE_var, font = ('calibre',10,'normal'))

MAIL_label = tk.Label(root, text = 'MAIL', font = ('calibre',10,'bold'))
MAIL_entry=tk.Entry(root, textvariable = MAIL_var, font = ('calibre',10,'normal'))

url_label = tk.Label(root, text = 'URL', font = ('calibre',10,'bold'))
url_entry=tk.Entry(root, textvariable = url_var, font = ('calibre',10,'normal'))

People_Counter_label = tk.Label(root, text = 'Show People Count', font = ('calibre',10,'bold'))
People_Counter_1=tk.Radiobutton(root, text="YES", variable=p, value= True)#.pack(anchor=W)
People_Counter_2=tk.Radiobutton(root, text="NO", variable=p, value= False)#.pack(anchor=W)

Thread_label = tk.Label(root, text = 'Show Serious Violations', font = ('calibre',10,'bold'))
Thread_1=tk.Radiobutton(root, text="YES", variable=v, value= True)#.pack(anchor=W)
Thread_2=tk.Radiobutton(root, text="NO", variable=v, value= False)#.pack(anchor=W)

ALERT_label = tk.Label(root, text = 'SHOW ALERT', font = ('calibre',10,'bold'))
ALERT_1=tk.Radiobutton(root, text="YES", variable=a, value= True)#.pack(anchor=W)
ALERT_2=tk.Radiobutton(root, text="NO", variable=a, value= False)#.pack(anchor=W)

USE_GPU_label = tk.Label(root, text = 'USE GPU', font = ('calibre',10,'bold'))
USE_GPU_1=tk.Radiobutton(root, text="YES", variable=u, value= True)#.pack(anchor=W)
USE_GPU_2=tk.Radiobutton(root, text="NO", variable=u, value= False)#.pack(anchor=W)

sub_btn=tk.Button(root,text = 'Submit', command= lambda : submit())
sub_btn.place(x=5,y=160)

Threshold_label.grid(row=0,column=0)
Threshold_entry.grid(row=0,column=1)
MAX_DISTANCE_label.grid(row=1,column=0)
MAX_DISTANCE_entry.grid(row=1,column=1)
MIN_DISTANCE_label.grid(row=2,column=0)
MIN_DISTANCE_entry.grid(row=2,column=1)
MAIL_label.grid(row=3,column=0)
MAIL_entry.grid(row=3,column=1)
url_label.grid(row=4,column=0)
url_entry.grid(row=4,column=1)
People_Counter_label.grid(row=5,column=0)
People_Counter_1.grid(row=5,column=1)
People_Counter_2.grid(row=5,column=2)
Thread_label.grid(row=6,column=0)
Thread_1.grid(row=6,column=1)
Thread_2.grid(row=6,column=2)
ALERT_label.grid(row=7,column=0)
ALERT_1.grid(row=7,column=1)
ALERT_2.grid(row=7,column=2)
USE_GPU_label.grid(row=8,column=0)
USE_GPU_1.grid(row=8,column=1)
USE_GPU_2.grid(row=8,column=2)
sub_btn.grid(row=9,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
