from tkinter import *

root=Tk()#This creates blank video

label_1=Label(root, text="Name")
label_2=Label(root, text="Password")

entry_1=Entry(root)
entry_2=Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c = Checkbutton(root, text="Keep me logged inn")
c.grid(columnspan=2)

def printName():
    print("Hello my name is tayyab")
    
button_1=Button(root, text="Print my name", command=printName)
button_1.grid()

root.mainloop()#This will just loop the main windov


"""button1=Button(topFrame, text="Button 1",fg="red")
button2=Button(topFrame, text="Button 2",fg="blue")
button3=Button(bottomFrame, text="Button 3",fg="green")
button4=Button(bottomFrame, text="Button 4",fg="purple")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
label_1=Label(root, text="Name")
label_2=Label(root, text="password")
entry_1=Entry(root)
entry_2=Entry(root)"""