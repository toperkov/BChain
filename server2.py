from socket import *
import asyncio
varijabla = 0
async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))
        print(varijabla)

async def echo_handler(client, loop):
    while True:
        global varijabla
        data = await loop.sock_recv(client, 10000)
        if not data:
            break
        data = data + bytes(varijabla)
        varijabla = varijabla + 1
        print(varijabla, "\n")
        await loop.sock_sendall(client, b'Got ' + data)
    print('Connection closed')
    client.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('', 60000), loop))
    