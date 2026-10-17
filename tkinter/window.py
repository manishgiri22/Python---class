from tkinter import*
window=Tk()         # to initalize the window to the user screen 
window.title("new GUI for the kids") # to make the window title 

window.geometry("500x500")
window.resizable(False,False)   # to make the window static to the user 

'''
l1=Label(window,text="edureka",font=("Arial Bold",50,"italic"),anchor="center")  #  label widget
l1.grid(column=2,row=1)

def clicked():
    l2=Label(window,text="button was clicked")
    l2.place(x=200,y=400)
bt2=Button(window,text="enter",command=clicked,bg="white",fg="red",font=("times new roman",50,"bold"))
bt2.grid(column=1,row=1)
bt=Button(window,text="enter" ,bg="red",fg="yellow")
bt.grid(column=1,row=0)
# using grid setting the posintion 


'''

# creating the text box to take input from the user 
txt=Entry(window)
txt.pack(side=TOP,padx=20,pady=20)

def show():
    l3=Label(window,text=txt.get,fg='black',font=("Times new roman",39,"bold"),anchor="center")
click=Button(window,text="click",fg="red",bg="yellow",command=show)
click.pack(side=TOP)


ch1=Checkbutton(window,text="use in login")

red1=Radiobutton(window,text="python")
red2=Radiobutton(window,text="java")
red1.pack(side=TOP)
red2.pack(side=TOP)



txt=scrolledtext.ScrolledText(window,text="python tkinter module training",width=40,height=10)

window.mainloop()
