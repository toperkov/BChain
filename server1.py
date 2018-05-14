from socket import *
import asyncio
import json
import pickle

ip = '127.0.0.1'

bChainServersList = []
bChainServersList.append("127.0.0.5")
bChainServersList.append("127.0.0.5")
bChainServersList.append("127.0.0.4")
bChainServersList.append("127.0.0.2")
bChainServersList.append("127.0.0.3")

controlList = ["0.0.0.0"]

# create a socket object
async def SendAllIpAddr(addr, loop):
    print("Ulaz u SendAllIpAddr\n")
    noviSocket = socket(AF_INET, SOCK_STREAM)
    noviSocket.connect((ip, 30000))

    b = json.dumps(bChainServersList).encode('utf-8')
    await loop.sock_sendall(noviSocket, b)

    noviSocket.close()
    print("zavrsio\n")

async def SendControlList(addr, loop):#saljemo kada je novi server
    print("Ulaz u SendAllIpAddr\n")   #vec inicijaliziran
    noviSocket = socket(AF_INET, SOCK_STREAM)
    noviSocket.connect((ip, 30000))

    b = json.dumps(controlList).encode('utf-8')
    await loop.sock_sendall(noviSocket, b)

    noviSocket.close()
    print("zavrsio\n")

async def AddToBChain(addr, loop):
    print("ulaz u AddToBChain\n")
    for i in bChainServersList:
        if i == addr[0]:
            loop.create_task(SendControlList(addr, loop))
            return
        
    bChainServersList.append(addr[0])
    loop.create_task(SendAllIpAddr(addr, loop))


async def echo_server(address, loop):
    print("echo_server")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(request_handler(client, addr, loop))

async def request_handler(client, addr, loop):
    global data
    print("request handler")
    data = await loop.sock_recv(client, 1024)

    data = data.decode()
    print("primio sam {}", format(data))
    if data == "INIT":
        print("usao sam i u init")
        loop.create_task(AddToBChain(addr, loop))
        print("prosao sam funkiju")
    elif data == "TRANS":
        pass
    elif data == "BLOCK":
        pass
    else:
        loop.create_task(govno(loop))
    print('Connection closed')
    client.close()

async def govno(loop):
    print("sranje")



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop2 = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('', 9999), loop))

    