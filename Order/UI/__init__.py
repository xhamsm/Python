import tkinter as tk
import Post.SendPost as ps
import Post.ConfigParser as pc

class OrderFrame(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)

        tk.Frame(height=200, width=400).pack()
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        self.order=tk.Button(self,command=self.clickMe)
        self.orderNomarl=tk.Button(self,text="test").pack(side="left")
        self.content=tk.Entry(self,width=50)
        self.order["text"]="Order"
        self.order.pack(side="top")
        self.content.pack(side="bottom")

    def clickMe(self):
        self.content.insert(0,ps.sendPost())

root = tk.Tk()
of=OrderFrame(master=root)
of.mainloop()