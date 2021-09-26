from tkinter import*
win = Tk()
win.config(bg="white")
def ok():
    t=en.get()
    lb.config(text=t)

lb = Label(bg="white",fg="black",text="pipi")
lb.pack()
en=Entry()
en.pack()

#def say_hi ():
    #print("pupu")

#img=PhotoImage(file="unnamed.jpg")
btn=Button(text="ok",command=ok)
#btn.config(image=img)

#btn.config(command=say_hi)
btn.pack()


win.mainloop()