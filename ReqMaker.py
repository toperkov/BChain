import socket

flag = True

while flag:
    flag = int(input('\n 0 - exit \n 1 - make transation'))
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect(("", 9999))
    sender = input("Enter your ID")
    receiver = input("Enter receiver's ID")
    amount = "Enter coin number"
    trans = "TRANS" + "," + sender + "," + receiver + "," + amount
    socket.sendall(trans.encode('ascii'))
    socket.close()