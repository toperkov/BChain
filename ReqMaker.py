import socket
from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
                      
    def create_widgets(self):

        self.myId = "nestoNestoNesto" ##todo: shoudl not be hardcoded

        self.myIdLabel = Label(self,text="MyId:")
        self.myIdLabel.grid(row=0, column=0)

        self.myId = Label(self, text=self.myId)
        self.myId.grid(row=0, column=1)

        self.ReceiverIdLabel = Label(self, text="ReceiverId:")
        self.ReceiverIdLabel.grid(row=1, column=0)
         
        self.receiverIdEntry = Entry(self,width=50)
        self.receiverIdEntry.grid(row=1, column=1)

        self.amountLabel = Label(self, text="Amount:")
        self.amountLabel.grid(row=2, column=0)
         
        self.amountEntry = Entry(self,width=50)
        self.amountEntry.grid(row=2, column=1)

        self.transactionSubmitButton = Button(self, \
                                              text="Submit transaction", \
                                              )
        self.transactionSubmitButton["command"] = self.SubmitTransaction
        self.transactionSubmitButton.grid(row=3, column=0)

        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(row=3, column=1)
    def say_hi(self):
        print("hi there, everyone!")

    def SubmitTransaction(self):
        myId = self.myId
        receiverId = self.receiverIdEntry.get()
        amount = self.amountEntry.get()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", 9999))
        trans = "TRANS" + "," + myID + "," + receiverId + "," + amount
        sock.sendall(trans.encode('ascii'))
        sock.close()

root = Tk()
app = Application(master=root)
app.mainloop()
