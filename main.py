from tkinter import*
screen=Tk()
screen.title("Addind Widgets")
screen.geometry("500x400")
L1=Label(text="Welcome to Kick",bg="dark blue",fg="white")
L1.pack()
L2=Label(text="Enter Your Username",bg="red",fg="black")
L2.pack()
E1=Entry()
E1.pack()
textbox=Text(height=3)
textbox.pack()
def display():
    name=E1.get()
    greet="Hello "+name+" Welcome to Kick"
    textbox.insert(1.0,greet)
B1=Button(text="Star Streaming",command=display) 
B1.pack()
screen.mainloop()
