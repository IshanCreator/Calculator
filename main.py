from tkinter import *
import tkinter
from tkinter import messagebox 

root=tkinter.Tk()
root.geometry("500x750")
root.title("Calculator Somthing New")
photo = PhotoImage(file = "logo.png ")
root.iconphoto(False, photo)




# ----------- Def click Event -------

def click(event):
    global scvalue
    text=event.widget.cget("text")
    # print(text)
    try:
        if text=="=":
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                value=eval(screen.get())

            scvalue.set(value)
            screen.update
        elif text=="DeL":
            scvalue.set("")
            screen.update
        
        else:
            scvalue.set(scvalue.get()+text)
            screen.update
    except:
        messagebox.showinfo("ooops","Somthing went wrong")
    

# ---------- set str -------------
scvalue=StringVar()
scvalue.set("")

# ------------ Entry Screen ------------

Label(root,text="Calculator ",font=("Comic Sans MS",30),fg="orange").pack()

screen=Entry(root,textvariable=scvalue,font=("Comic Sans MS",30),bg="gray")
screen.place(x=10,y=100)

# --------------------------------------------------------- Button ---------
f0=Frame(root,bg="peach puff")
f0.place(x=0,y=750,width=500,height=750)
f1=Frame(root,bg="purple")   # First we create frame for button
f1.place(x=10,y=200,width=480,height=530)

                        # --------------- Button Row Zero

b=Button(f1,text="9",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=0,column=0)
b.bind("<Button-1>",click)


b=Button(f1,text="8",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=0,column=1)
b.bind("<Button-1>",click)


b=Button(f1,text="7",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=0,column=2)
b.bind("<Button-1>",click)



                        # --------------- Button Row One

b=Button(f1,text="6",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=1,column=0)
b.bind("<Button-1>",click)


b=Button(f1,text="5",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=1,column=1)
b.bind("<Button-1>",click)


b=Button(f1,text="4",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=1,column=2)
b.bind("<Button-1>",click)


                        # --------------- Button Row Two

b=Button(f1,text="3",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=2,column=0)
b.bind("<Button-1>",click)


b=Button(f1,text="2",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=2,column=1)
b.bind("<Button-1>",click)


b=Button(f1,text="1",bg="black",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=2,column=2)
b.bind("<Button-1>",click)



                        # --------------- symbals


b=Button(f1,text="/",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=0,column=4)
b.bind("<Button-1>",click)

b=Button(f1,text="+",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=1,column=4)
b.bind("<Button-1>",click)


b=Button(f1,text="-",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=2,column=4)
b.bind("<Button-1>",click)



b=Button(f1,text=".",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=3,column=0)
b.bind("<Button-1>",click)



b=Button(f1,text="0",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=3,column=1)
b.bind("<Button-1>",click)


b=Button(f1,text="*",bg="orange",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.grid(row=3,column=2)
b.bind("<Button-1>",click)


b=Button(f1,text="DeL",bg="red",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=4,relief=RAISED,borderwidth=5)
b.place(x=350,y=320)
b.bind("<Button-1>",click)


b=Button(f1,text="=",bg="magenta2",fg="white",font=("Comic Sans MS",30),cursor="hand2",width=17,height=int(0.1),relief=RAISED,borderwidth=5)
b.place(x=15,y=430)
b.bind("<Button-1>",click)











root.mainloop()