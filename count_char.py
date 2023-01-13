from tkinter import *
 

def frame(root,side):
    w = Frame(root)
    w.pack(side=side,expand=YES,fill=BOTH)


class count(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Count character")
        self.pack(expand=YES,fill=BOTH)

        display = StringVar()
        Entry(self,justify=CENTER,font="20",fg='green',width=40,relief=SUNKEN,textvariable=display).pack(side=TOP,expand=YES,fill=BOTH,)

        result = StringVar()
        Label(self,font="20",fg='green',width=40,relief=SUNKEN,textvariable=result).pack(side=BOTTOM,expand=YES,fill=BOTH)


if __name__=="__main__":
    root = Tk()
    view = count(root)
    view.pack()
    view.mainloop()
