#!/usr/bin/python3           # This is server.py file
import socket              
import pickle
import json
ip = '127.0.0.1'

bChainServersList = []
bChainServersList.append("127.0.0.5")
bChainServersList.append("127.0.0.5")
bChainServersList.append("127.0.0.4")
bChainServersList.append("127.0.0.2")
bChainServersList.append("127.0.0.3")

# create a socket object
def SendAllIpAddr(addr):
    print("Ulaz u SendAllIpAddr\n")
    noviSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    noviSocket.connect((ip, 30000))

    b = json.dumps(bChainServersList).encode('utf-8')
    noviSocket.sendall(b)

    # for i in bChainServersList:
    #     noviSocket.sendall(i.encode())
    noviSocket.close()

def AddToBChain(addr):
    print("ulaz u AddToBChain\n")
    for i in bChainServersList:
        if i == addr[0]:
            print("Vec ste dodani u server")
#server koji nije stalno na mrezi se kaznjava na nacin da
#ne moze stalno slati zahtjeve za konekcije
            return
        
    bChainServersList.append(addr[0])
    SendAllIpAddr(addr)



def main():
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = ""                           

    port = 9999                                           

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        # establish a connection
        clientsocket,addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))
        
        print("DODATAK: ", str(clientsocket), "\n")
        
        poruka = clientsocket.recv(1024)
        poruka = poruka.decode('ascii')
        print(type(poruka))
        if poruka == "INIT":
            AddToBChain(addr)
        print("prosli smo funkciju")

        clientsocket.close()

if __name__ == "__main__":
    main()