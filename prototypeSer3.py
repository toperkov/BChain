#!/usr/bin/python3           # This is client.py file

import socket
import json

ip = '127.0.0.1'
initilized = False
bChainServersList = []
# create a socket object
def sendIpAddr(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 
    s.sendall("INIT".encode('ascii'))
    s.close()

# get local machine name


# connection to hostname on the port.
                              
flag = 1
while (flag != 0):
    print("usao sam u while\n")
    flag = int(input("Unesite sta zelite: 1 - salji poruku, 0 - izlaz"))

    if(flag == 1):
        host = ""       
        print(host)                       
        port = 9999
        sendIpAddr(host, port)
        
        recSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        recSocket.bind((ip, 30000))
        recSocket.listen(5)
        
        nesto, adresa = recSocket.accept()
        b = b''
        while True:
            print("usao sam u while petlju\n")
            tmp = nesto.recv(1024)
            if not tmp:
                break
            b = b + tmp

            print("Doasao sam do kraja while petlje\n")
        d = json.loads(b.decode('utf-8'))
        print(d)
        if "0.0.0.0" not in d:
            bChainServersList = d
            print(bChainServersList)
        else:
            print("Vasa IP adreasa je vec dodana u BChain")
        recSocket.close()
