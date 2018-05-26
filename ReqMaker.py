import socket
from tkinter import *

def SendTransaction(yourID, receiverID, amount):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(("", 9999))
    trans = "TRANS" + "," + yourID + "," + receiverID + "," + amount
    socket.sendall(trans.encode('ascii'))
    socket.close()


window = Tk()

yourID = "nestoNestoNesto"
 
window.geometry('500x200')
 
lbl1 = Label(window, text="YourID:")
 
lbl1.grid(column=0, row=0)

lblYourID = Label(window, text=yourID)

lblYourID.grid(column=1, row=0)

lbl2 = Label(window, text="ReceiverID:")
 
lbl2.grid(column=0, row=1)
 
receiverID = Entry(window,width=50)
 
receiverID.grid(column=1, row=1)

lbl3 = Label(window, text="Amount:")
 
lbl3.grid(column=0, row=2)
 
Amount = Entry(window,width=50)

Amount.grid(column=1, row=2)
Amount.grid(column=1, row=2)


 
btn = Button(window, text="Send transaction",\
 command=SendTransaction)
 
btn.grid(column=0, row=3)
 
window.mainloop()
