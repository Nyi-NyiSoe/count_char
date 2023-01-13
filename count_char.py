from tkinter import *
 

def frame(root,side):
    w = Frame(root)
    w.pack(side=side,expand=YES,fill=BOTH)

def button(root,side,text,command=None):
    w = Button(root,width=10,text=text,command=command)
    w.pack(side=side,expand=YES,fill=BOTH)
    return w

def count(char):
    arr={}
    for i in char:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1
    return arr
    



class count_char(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        master.geometry("1000x400")
        self.master.title("Count character")
        self.pack(expand=YES,fill=BOTH)

        display = StringVar()
        Entry(self,justify=CENTER,font="20",fg='green',width=40,relief=SUNKEN,textvariable=display).pack(side=TOP,expand=YES,fill=BOTH,)

        result = StringVar()
        Label(self,font="20",fg='green',width=40,relief=SUNKEN,textvariable=result).pack(side=RIGHT,expand=YES,fill=BOTH)


        button(frame(self,TOP),LEFT,"BackSpace",lambda w =display:w.set(w.get()[:-1]))
        button(frame(self,TOP),RIGHT,"Submit",lambda r=result,w=display:r.set(count(w.get())))
        button(frame(self,TOP),RIGHT,"Delete",lambda w=display:w.set(""))

if __name__=="__main__":
    root = Tk()
    view = count_char(root)
    view.pack()
    view.mainloop()
