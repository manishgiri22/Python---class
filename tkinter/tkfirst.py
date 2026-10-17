from tkinter import*
root=Tk()           # to create a small window for the user 
root.title("first gui class")
root.geometry("900x600")
root.wm_iconbitmap("chatgpt.ico")   # to insert ico icon to the window
root.resizable(False,False)  # to make the static window 


# PACK IN TKINTER 
'''

lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.pack(side=LEFT)

lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.pack(side=RIGHT)

lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.pack(side=BOTTOM)

'''

# GRID IN TKINTER 
'''
lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.grid(row=0,column=0)


lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.grid(row=0,column=1)

lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.grid(row=1,column=0)

lb1=Label(root,text=" tkinter class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.grid(row=2,column=5)

'''
 
#place in tkinter
lb1=Label(root,text=" tkinter place class",anchor="center",font=("times new roman",20,"bold"),fg="red")
lb1.place(x=320,y=320)

enter=Entry(root)       # Entry is same as input functioon in python 
enter.pack(padx=30,pady=30)


def click():                                #enter.get is used to get text from the enter entry
    lb2=Label(root,text=enter.get(),anchor="center",font=("times new roman",20,"italic"))
    lb2.pack()
    

b1=Button(root,text="click me", fg="red",bg="yellow", font=("times new roman",20,"bold"),command=click)     #Button in the tkinter 
b1.pack(side=BOTTOM)
# b1.place(x=240,y=100)


root.mainloop()         #it holds window for the user same as getch()
